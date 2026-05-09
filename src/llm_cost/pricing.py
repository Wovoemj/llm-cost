"""Model pricing data (per 1M tokens in USD). Prices as of 2026-05."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ModelPricing:
    """Pricing for a single model."""
    name: str
    provider: str
    input_price: float   # USD per 1M input tokens
    output_price: float  # USD per 1M output tokens
    context_window: int
    tokenizer: str = "cl100k_base"  # tiktoken encoding name
    max_output: Optional[int] = None


# ─── OpenAI ───────────────────────────────────────────────────────────
MODELS: dict[str, ModelPricing] = {
    # GPT-4o family
    "gpt-4o": ModelPricing("gpt-4o", "OpenAI", 2.50, 10.00, 128_000, "o200k_base"),
    "gpt-4o-mini": ModelPricing("gpt-4o-mini", "OpenAI", 0.15, 0.60, 128_000, "o200k_base"),
    "gpt-4o-2024-11-20": ModelPricing("gpt-4o-2024-11-20", "OpenAI", 2.50, 10.00, 128_000, "o200k_base"),
    "gpt-4o-mini-2024-07-18": ModelPricing("gpt-4o-mini-2024-07-18", "OpenAI", 0.15, 0.60, 128_000, "o200k_base"),

    # GPT-4.1 family
    "gpt-4.1": ModelPricing("gpt-4.1", "OpenAI", 2.00, 8.00, 1_048_576, "o200k_base"),
    "gpt-4.1-mini": ModelPricing("gpt-4.1-mini", "OpenAI", 0.40, 1.60, 1_048_576, "o200k_base"),
    "gpt-4.1-nano": ModelPricing("gpt-4.1-nano", "OpenAI", 0.10, 0.40, 1_048_576, "o200k_base"),

    # o-series (reasoning)
    "o1": ModelPricing("o1", "OpenAI", 15.00, 60.00, 200_000, "o200k_base"),
    "o1-mini": ModelPricing("o1-mini", "OpenAI", 3.00, 12.00, 128_000, "o200k_base"),
    "o1-pro": ModelPricing("o1-pro", "OpenAI", 150.00, 600.00, 200_000, "o200k_base"),
    "o3": ModelPricing("o3", "OpenAI", 10.00, 40.00, 200_000, "o200k_base"),
    "o3-mini": ModelPricing("o3-mini", "OpenAI", 1.10, 4.40, 200_000, "o200k_base"),
    "o4-mini": ModelPricing("o4-mini", "OpenAI", 1.10, 4.40, 200_000, "o200k_base"),

    # GPT-4 Turbo (legacy)
    "gpt-4-turbo": ModelPricing("gpt-4-turbo", "OpenAI", 10.00, 30.00, 128_000, "cl100k_base"),
    "gpt-4": ModelPricing("gpt-4", "OpenAI", 30.00, 60.00, 8_192, "cl100k_base"),
    "gpt-3.5-turbo": ModelPricing("gpt-3.5-turbo", "OpenAI", 0.50, 1.50, 16_385, "cl100k_base"),

    # ─── Anthropic ────────────────────────────────────────────────────
    "claude-opus-4": ModelPricing("claude-opus-4", "Anthropic", 15.00, 75.00, 200_000),
    "claude-sonnet-4": ModelPricing("claude-sonnet-4", "Anthropic", 3.00, 15.00, 200_000),
    "claude-3.5-sonnet": ModelPricing("claude-3.5-sonnet", "Anthropic", 3.00, 15.00, 200_000),
    "claude-3.5-haiku": ModelPricing("claude-3.5-haiku", "Anthropic", 0.80, 4.00, 200_000),
    "claude-3-opus": ModelPricing("claude-3-opus", "Anthropic", 15.00, 75.00, 200_000),
    "claude-3-sonnet": ModelPricing("claude-3-sonnet", "Anthropic", 3.00, 15.00, 200_000),
    "claude-3-haiku": ModelPricing("claude-3-haiku", "Anthropic", 0.25, 1.25, 200_000),

    # ─── Google ───────────────────────────────────────────────────────
    "gemini-2.5-pro": ModelPricing("gemini-2.5-pro", "Google", 1.25, 10.00, 1_048_576),
    "gemini-2.5-flash": ModelPricing("gemini-2.5-flash", "Google", 0.15, 0.60, 1_048_576),
    "gemini-2.0-flash": ModelPricing("gemini-2.0-flash", "Google", 0.10, 0.40, 1_048_576),
    "gemini-1.5-pro": ModelPricing("gemini-1.5-pro", "Google", 1.25, 5.00, 2_097_152),
    "gemini-1.5-flash": ModelPricing("gemini-1.5-flash", "Google", 0.075, 0.30, 1_048_576),

    # ─── DeepSeek ─────────────────────────────────────────────────────
    "deepseek-v3": ModelPricing("deepseek-v3", "DeepSeek", 0.27, 1.10, 128_000),
    "deepseek-r1": ModelPricing("deepseek-r1", "DeepSeek", 0.55, 2.19, 128_000),

    # ─── Mistral ──────────────────────────────────────────────────────
    "mistral-large": ModelPricing("mistral-large", "Mistral", 2.00, 6.00, 128_000),
    "mistral-small": ModelPricing("mistral-small", "Mistral", 0.10, 0.30, 128_000),
    "codestral": ModelPricing("codestral", "Mistral", 0.30, 0.90, 256_000),

    # ─── xAI ──────────────────────────────────────────────────────────
    "grok-3": ModelPricing("grok-3", "xAI", 3.00, 15.00, 131_072),
    "grok-3-mini": ModelPricing("grok-3-mini", "xAI", 0.30, 0.50, 131_072),
}


# ─── Aliases ──────────────────────────────────────────────────────────
ALIASES: dict[str, str] = {
    "gpt4o": "gpt-4o",
    "gpt-4o-latest": "gpt-4o",
    "claude-opus": "claude-opus-4",
    "claude-sonnet": "claude-sonnet-4",
    "gemini-pro": "gemini-2.5-pro",
    "gemini-flash": "gemini-2.5-flash",
    "deepseek": "deepseek-v3",
    "r1": "deepseek-r1",
}


def get_model(name: str) -> ModelPricing:
    """Resolve model by name or alias. Raises KeyError if not found."""
    name_lower = name.lower().strip()
    resolved = ALIASES.get(name_lower, name_lower)
    if resolved not in MODELS:
        available = sorted(MODELS.keys())
        raise KeyError(
            f"Unknown model '{name}'. Available:\n  " + "\n  ".join(available)
        )
    return MODELS[resolved]


def list_models(provider: Optional[str] = None) -> list[ModelPricing]:
    """List all models, optionally filtered by provider."""
    models = list(MODELS.values())
    if provider:
        models = [m for m in models if m.provider.lower() == provider.lower()]
    return sorted(models, key=lambda m: (m.provider, m.input_price))
