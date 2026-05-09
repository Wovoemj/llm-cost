"""Core cost calculation logic."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from .pricing import get_model, ModelPricing
from .tokens import count_tokens, count_message_tokens, estimate_output_tokens


@dataclass
class CostResult:
    """Result of a cost estimation."""
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    input_cost: float
    output_cost: float
    total_cost: float
    context_window: int
    context_usage_pct: float

    @property
    def total_cost_display(self) -> str:
        if self.total_cost < 0.01:
            return f"${self.total_cost:.6f}"
        elif self.total_cost < 1.0:
            return f"${self.total_cost:.4f}"
        else:
            return f"${self.total_cost:.2f}"

    @property
    def fits_context(self) -> bool:
        return self.input_tokens <= self.context_window

    def to_daily(self, calls_per_day: int = 100) -> float:
        return self.total_cost * calls_per_day

    def to_monthly(self, calls_per_day: int = 100) -> float:
        return self.to_daily(calls_per_day) * 30


def estimate_cost(
    text: str,
    model_name: str,
    output_ratio: float = 0.5,
    max_output_tokens: Optional[int] = None,
    is_messages: bool = False,
    system_prompt: Optional[str] = None,
) -> CostResult:
    """Estimate the cost of a single API call.

    Args:
        text: The input text or message content.
        model_name: Model identifier (e.g. 'gpt-4o', 'claude-sonnet-4').
        output_ratio: Estimated output/input token ratio (default 0.5).
        max_output_tokens: Cap estimated output tokens.
        is_messages: If True, text is treated as already tokenized message format.
        system_prompt: Optional system prompt to prepend to token count.
    """
    model = get_model(model_name)

    # Combine system prompt + user text for token counting
    full_text = text
    if system_prompt:
        full_text = system_prompt + "\n\n" + text

    # Count input tokens
    if is_messages:
        # Assume text is already in message list format (JSON)
        import json
        try:
            messages = json.loads(text) if isinstance(text, str) else text
            if system_prompt:
                messages = [{"role": "system", "content": system_prompt}] + messages
            input_tokens = count_message_tokens(messages, model.tokenizer, model.name)
        except (json.JSONDecodeError, TypeError):
            input_tokens = count_tokens(full_text, model.tokenizer)
    else:
        input_tokens = count_tokens(full_text, model.tokenizer)

    # Estimate output tokens
    if max_output_tokens is None:
        max_output_tokens = model.max_output
    output_tokens = estimate_output_tokens(input_tokens, output_ratio, max_output_tokens)

    # Calculate costs (pricing is per 1M tokens)
    input_cost = (input_tokens / 1_000_000) * model.input_price
    output_cost = (output_tokens / 1_000_000) * model.output_price
    total_cost = input_cost + output_cost

    ctx_pct = (input_tokens / model.context_window) * 100 if model.context_window else 0

    return CostResult(
        model=model.name,
        provider=model.provider,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        input_cost=input_cost,
        output_cost=output_cost,
        total_cost=total_cost,
        context_window=model.context_window,
        context_usage_pct=round(ctx_pct, 1),
    )


def compare_models(
    text: str,
    model_names: list[str],
    output_ratio: float = 0.5,
    system_prompt: Optional[str] = None,
) -> list[CostResult]:
    """Compare cost across multiple models for the same input."""
    results = []
    for name in model_names:
        try:
            result = estimate_cost(text, name, output_ratio, system_prompt=system_prompt)
            results.append(result)
        except KeyError:
            continue
    return sorted(results, key=lambda r: r.total_cost)


def estimate_file_cost(
    filepath: str,
    model_name: str,
    output_ratio: float = 0.5,
    system_prompt: Optional[str] = None,
) -> CostResult:
    """Estimate cost for processing a file's contents."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return estimate_cost(text, model_name, output_ratio, system_prompt=system_prompt)
