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
    # GPT-5.5 family (2026)
    "gpt-5.5": ModelPricing("gpt-5.5", "OpenAI", 5.00, 30.00, 272_000, "o200k_base"),
    "gpt-5.5-pro": ModelPricing("gpt-5.5-pro", "OpenAI", 30.00, 180.00, 272_000, "o200k_base"),

    # GPT-5.4 family (2026)
    "gpt-5.4": ModelPricing("gpt-5.4", "OpenAI", 2.50, 15.00, 1_048_576, "o200k_base"),
    "gpt-5.4-mini": ModelPricing("gpt-5.4-mini", "OpenAI", 0.75, 4.50, 1_048_576, "o200k_base"),
    "gpt-5.4-nano": ModelPricing("gpt-5.4-nano", "OpenAI", 0.20, 1.25, 1_048_576, "o200k_base"),
    "gpt-5.4-pro": ModelPricing("gpt-5.4-pro", "OpenAI", 30.00, 180.00, 262_144, "o200k_base"),

    # GPT-5 family (2025)
    "gpt-5": ModelPricing("gpt-5", "OpenAI", 1.25, 10.00, 128_000, "o200k_base"),
    "gpt-5-mini": ModelPricing("gpt-5-mini", "OpenAI", 0.25, 2.00, 128_000, "o200k_base"),
    "gpt-5-nano": ModelPricing("gpt-5-nano", "OpenAI", 0.05, 0.40, 32_000, "o200k_base"),

    # GPT-4.1 family
    "gpt-4.1": ModelPricing("gpt-4.1", "OpenAI", 2.00, 8.00, 1_048_576, "o200k_base"),
    "gpt-4.1-mini": ModelPricing("gpt-4.1-mini", "OpenAI", 0.40, 1.60, 1_048_576, "o200k_base"),
    "gpt-4.1-nano": ModelPricing("gpt-4.1-nano", "OpenAI", 0.10, 0.40, 1_048_576, "o200k_base"),

    # GPT-4o family
    "gpt-4o": ModelPricing("gpt-4o", "OpenAI", 2.50, 10.00, 128_000, "o200k_base"),
    "gpt-4o-mini": ModelPricing("gpt-4o-mini", "OpenAI", 0.15, 0.60, 128_000, "o200k_base"),
    "gpt-4o-2024-11-20": ModelPricing("gpt-4o-2024-11-20", "OpenAI", 2.50, 10.00, 128_000, "o200k_base"),
    "gpt-4o-mini-2024-07-18": ModelPricing("gpt-4o-mini-2024-07-18", "OpenAI", 0.15, 0.60, 128_000, "o200k_base"),

    # o-series (reasoning)
    "o4-mini": ModelPricing("o4-mini", "OpenAI", 1.10, 4.40, 200_000, "o200k_base"),
    "o3": ModelPricing("o3", "OpenAI", 2.00, 8.00, 200_000, "o200k_base"),
    "o3-mini": ModelPricing("o3-mini", "OpenAI", 1.10, 4.40, 200_000, "o200k_base"),
    "o3-pro": ModelPricing("o3-pro", "OpenAI", 20.00, 80.00, 262_144, "o200k_base"),
    "o1": ModelPricing("o1", "OpenAI", 15.00, 60.00, 200_000, "o200k_base"),
    "o1-mini": ModelPricing("o1-mini", "OpenAI", 3.00, 12.00, 128_000, "o200k_base"),
    "o1-pro": ModelPricing("o1-pro", "OpenAI", 150.00, 600.00, 200_000, "o200k_base"),

    # Codex
    "codex-mini": ModelPricing("codex-mini", "OpenAI", 1.50, 6.00, 128_000, "o200k_base"),

    # GPT-4 Turbo (legacy)
    "gpt-4-turbo": ModelPricing("gpt-4-turbo", "OpenAI", 10.00, 30.00, 128_000, "cl100k_base"),
    "gpt-4": ModelPricing("gpt-4", "OpenAI", 30.00, 60.00, 8_192, "cl100k_base"),
    "gpt-3.5-turbo": ModelPricing("gpt-3.5-turbo", "OpenAI", 0.50, 1.50, 16_385, "cl100k_base"),

    # ─── Anthropic ────────────────────────────────────────────────────
    "claude-opus-4.7": ModelPricing("claude-opus-4.7", "Anthropic", 5.00, 25.00, 1_000_000),
    "claude-opus-4.6": ModelPricing("claude-opus-4.6", "Anthropic", 5.00, 25.00, 1_000_000),
    "claude-opus-4.5": ModelPricing("claude-opus-4.5", "Anthropic", 5.00, 25.00, 1_000_000),
    "claude-opus-4": ModelPricing("claude-opus-4", "Anthropic", 15.00, 75.00, 200_000),
    "claude-sonnet-4.6": ModelPricing("claude-sonnet-4.6", "Anthropic", 3.00, 15.00, 1_000_000),
    "claude-sonnet-4": ModelPricing("claude-sonnet-4", "Anthropic", 3.00, 15.00, 200_000),
    "claude-3.5-sonnet": ModelPricing("claude-3.5-sonnet", "Anthropic", 3.00, 15.00, 200_000),
    "claude-haiku-4.5": ModelPricing("claude-haiku-4.5", "Anthropic", 1.00, 5.00, 1_000_000),
    "claude-3.5-haiku": ModelPricing("claude-3.5-haiku", "Anthropic", 0.80, 4.00, 200_000),
    "claude-3-opus": ModelPricing("claude-3-opus", "Anthropic", 15.00, 75.00, 200_000),
    "claude-3-sonnet": ModelPricing("claude-3-sonnet", "Anthropic", 3.00, 15.00, 200_000),
    "claude-3-haiku": ModelPricing("claude-3-haiku", "Anthropic", 0.25, 1.25, 200_000),

    # ─── Google Gemini ────────────────────────────────────────────────
    "gemini-3.1-pro": ModelPricing("gemini-3.1-pro", "Google", 2.00, 12.00, 1_048_576),
    "gemini-3-flash": ModelPricing("gemini-3-flash", "Google", 0.50, 3.00, 1_048_576),
    "gemini-3.1-flash-lite": ModelPricing("gemini-3.1-flash-lite", "Google", 0.25, 1.50, 1_048_576),
    "gemini-2.5-pro": ModelPricing("gemini-2.5-pro", "Google", 1.25, 10.00, 1_048_576),
    "gemini-2.5-flash": ModelPricing("gemini-2.5-flash", "Google", 0.30, 2.50, 1_048_576),
    "gemini-2.5-flash-lite": ModelPricing("gemini-2.5-flash-lite", "Google", 0.10, 0.40, 1_048_576),
    "gemini-2.0-flash": ModelPricing("gemini-2.0-flash", "Google", 0.10, 0.40, 1_048_576),
    "gemini-1.5-pro": ModelPricing("gemini-1.5-pro", "Google", 1.25, 5.00, 2_097_152),
    "gemini-1.5-flash": ModelPricing("gemini-1.5-flash", "Google", 0.075, 0.30, 1_048_576),

    # ─── DeepSeek ─────────────────────────────────────────────────────
    "deepseek-v4-pro": ModelPricing("deepseek-v4-pro", "DeepSeek", 0.435, 0.87, 1_000_000),
    "deepseek-v4-flash": ModelPricing("deepseek-v4-flash", "DeepSeek", 0.14, 0.28, 1_000_000),
    "deepseek-v3": ModelPricing("deepseek-v3", "DeepSeek", 0.27, 1.10, 128_000),
    "deepseek-r1": ModelPricing("deepseek-r1", "DeepSeek", 0.55, 2.19, 128_000),

    # ─── Mistral ──────────────────────────────────────────────────────
    "magistral-medium": ModelPricing("magistral-medium", "Mistral", 2.00, 5.00, 40_000),
    "mistral-large-3": ModelPricing("mistral-large-3", "Mistral", 0.50, 1.50, 262_000),
    "mistral-medium-3.1": ModelPricing("mistral-medium-3.1", "Mistral", 0.40, 2.00, 131_000),
    "mistral-medium-3": ModelPricing("mistral-medium-3", "Mistral", 0.40, 2.00, 131_000),
    "codestral": ModelPricing("codestral", "Mistral", 0.30, 0.90, 256_000),
    "mistral-small-3.2": ModelPricing("mistral-small-3.2", "Mistral", 0.075, 0.20, 131_000),
    "mistral-small-3.1": ModelPricing("mistral-small-3.1", "Mistral", 0.10, 0.30, 128_000),
    "mistral-nemo": ModelPricing("mistral-nemo", "Mistral", 0.02, 0.03, 131_000),
    # Legacy names
    "mistral-large": ModelPricing("mistral-large", "Mistral", 0.50, 1.50, 262_000),
    "mistral-small": ModelPricing("mistral-small", "Mistral", 0.10, 0.30, 128_000),

    # ─── xAI (Grok) ──────────────────────────────────────────────────
    "grok-4.3": ModelPricing("grok-4.3", "xAI", 1.25, 2.50, 1_048_576),
    "grok-4.20": ModelPricing("grok-4.20", "xAI", 1.25, 2.50, 2_000_000),
    "grok-4.1-fast": ModelPricing("grok-4.1-fast", "xAI", 0.20, 0.50, 2_000_000),
    "grok-3": ModelPricing("grok-3", "xAI", 3.00, 15.00, 131_072),
    "grok-3-mini": ModelPricing("grok-3-mini", "xAI", 0.30, 0.50, 131_072),

    # ─── Cohere ───────────────────────────────────────────────────────
    "command-a": ModelPricing("command-a", "Cohere", 2.50, 10.00, 256_000),
    "command-r-plus": ModelPricing("command-r-plus", "Cohere", 2.50, 10.00, 128_000),
    "command-r": ModelPricing("command-r", "Cohere", 0.15, 0.60, 128_000),
    "command-r7b": ModelPricing("command-r7b", "Cohere", 0.037, 0.15, 128_000),

    # ─── Meta Llama (via third-party APIs) ────────────────────────────
    "llama-4-maverick": ModelPricing("llama-4-maverick", "Meta", 0.20, 0.75, 1_048_576),
    "llama-4-scout": ModelPricing("llama-4-scout", "Meta", 0.18, 0.70, 5_000_000),
    "llama-3.3-70b": ModelPricing("llama-3.3-70b", "Meta", 0.88, 0.88, 128_000),

    # ─── Amazon Nova (via AWS Bedrock) ────────────────────────────────
    "nova-2-lite": ModelPricing("nova-2-lite", "Amazon", 0.30, 2.50, 1_048_576),
    "nova-premier": ModelPricing("nova-premier", "Amazon", 8.00, 32.00, 200_000),
    "nova-pro": ModelPricing("nova-pro", "Amazon", 0.80, 3.20, 300_000),
    "nova-lite": ModelPricing("nova-lite", "Amazon", 0.06, 0.24, 300_000),
    "nova-micro": ModelPricing("nova-micro", "Amazon", 0.035, 0.14, 128_000),

    # ─── Perplexity ───────────────────────────────────────────────────
    "sonar": ModelPricing("sonar", "Perplexity", 1.00, 1.00, 128_000),
    "sonar-pro": ModelPricing("sonar-pro", "Perplexity", 3.00, 15.00, 200_000),
    "sonar-reasoning-pro": ModelPricing("sonar-reasoning-pro", "Perplexity", 2.00, 8.00, 128_000),
    "sonar-deep-research": ModelPricing("sonar-deep-research", "Perplexity", 2.00, 8.00, 128_000),

    # ─── Qwen (通义千问) ─────────────────────────────────────────────
    "qwen-max": ModelPricing("qwen-max", "Qwen", 1.04, 4.16, 32_000),
    "qwen-plus": ModelPricing("qwen-plus", "Qwen", 0.26, 0.78, 131_000),
    "qwen-turbo": ModelPricing("qwen-turbo", "Qwen", 0.10, 0.30, 131_000),

    # ─── Moonshot/Kimi (月之暗面) ────────────────────────────────────
    "kimi-k2.6": ModelPricing("kimi-k2.6", "Moonshot", 0.60, 2.50, 262_000),
    "kimi-k2-thinking": ModelPricing("kimi-k2-thinking", "Moonshot", 0.60, 2.50, 262_000),
    "kimi-k2-turbo": ModelPricing("kimi-k2-turbo", "Moonshot", 1.15, 8.00, 262_000),
    "moonshot-v1-128k": ModelPricing("moonshot-v1-128k", "Moonshot", 2.00, 5.00, 131_000),
    "moonshot-v1-32k": ModelPricing("moonshot-v1-32k", "Moonshot", 1.00, 3.00, 33_000),
    "moonshot-v1-8k": ModelPricing("moonshot-v1-8k", "Moonshot", 0.20, 2.00, 8_000),

    # ─── Zhipu/GLM (智谱) ───────────────────────────────────────────
    "glm-5.1": ModelPricing("glm-5.1", "Zhipu", 1.40, 4.40, 203_000),
    "glm-5": ModelPricing("glm-5", "Zhipu", 1.00, 3.20, 203_000),
    "glm-5-turbo": ModelPricing("glm-5-turbo", "Zhipu", 1.20, 4.00, 203_000),
    "glm-4.7": ModelPricing("glm-4.7", "Zhipu", 0.60, 2.20, 205_000),
    "glm-4.6": ModelPricing("glm-4.6", "Zhipu", 0.60, 2.20, 205_000),
    "glm-4.5": ModelPricing("glm-4.5", "Zhipu", 0.60, 2.20, 131_000),
    "glm-4.5-air": ModelPricing("glm-4.5-air", "Zhipu", 0.20, 1.10, 131_000),
    "glm-4.7-flash": ModelPricing("glm-4.7-flash", "Zhipu", 0.0, 0.0, 203_000),

    # ─── MiniMax ──────────────────────────────────────────────────────
    "minimax-m2.7": ModelPricing("minimax-m2.7", "MiniMax", 0.30, 1.20, 204_000),
    "minimax-m2.7-highspeed": ModelPricing("minimax-m2.7-highspeed", "MiniMax", 0.60, 2.40, 204_000),
    "minimax-m2.5": ModelPricing("minimax-m2.5", "MiniMax", 0.30, 1.20, 1_048_576),
    "minimax-m2.5-highspeed": ModelPricing("minimax-m2.5-highspeed", "MiniMax", 0.60, 2.40, 1_048_576),

    # ─── Baichuan (百川智能) ─────────────────────────────────────────
    "baichuan-m3-plus": ModelPricing("baichuan-m3-plus", "Baichuan", 0.69, 1.24, 32_000),
    "baichuan-m3": ModelPricing("baichuan-m3", "Baichuan", 1.38, 4.14, 32_000),
    "baichuan4-turbo": ModelPricing("baichuan4-turbo", "Baichuan", 2.07, 2.07, 32_000),
    "baichuan4-air": ModelPricing("baichuan4-air", "Baichuan", 0.14, 0.14, 32_000),
    "baichuan4": ModelPricing("baichuan4", "Baichuan", 13.80, 13.80, 32_000),

    # ─── Yi (零一万物) ───────────────────────────────────────────────
    "yi-large": ModelPricing("yi-large", "Yi", 3.00, 3.00, 32_000),
    "yi-large-turbo": ModelPricing("yi-large-turbo", "Yi", 0.60, 0.60, 32_000),
}


# ─── Aliases ──────────────────────────────────────────────────────────
ALIASES: dict[str, str] = {
    # OpenAI
    "gpt4o": "gpt-4o",
    "gpt-4o-latest": "gpt-4o",
    "gpt5": "gpt-5",
    "gpt-5-latest": "gpt-5.4",
    "gpt5.5": "gpt-5.5",
    "4o": "gpt-4o",
    "4o-mini": "gpt-4o-mini",
    "4.1": "gpt-4.1",
    "4.1-mini": "gpt-4.1-mini",
    "4.1-nano": "gpt-4.1-nano",
    "5.4": "gpt-5.4",
    "5.4-mini": "gpt-5.4-mini",
    "5.4-nano": "gpt-5.4-nano",

    # Anthropic
    "claude-opus": "claude-opus-4.7",
    "claude-sonnet": "claude-sonnet-4.6",
    "claude-haiku": "claude-haiku-4.5",
    "opus": "claude-opus-4.7",
    "sonnet": "claude-sonnet-4.6",
    "haiku": "claude-haiku-4.5",

    # Google
    "gemini-pro": "gemini-2.5-pro",
    "gemini-flash": "gemini-2.5-flash",
    "gemini-flash-lite": "gemini-2.5-flash-lite",
    "gemini": "gemini-2.5-pro",

    # DeepSeek
    "deepseek": "deepseek-v3",
    "r1": "deepseek-r1",
    "v3": "deepseek-v3",
    "v4": "deepseek-v4-pro",
    "v4-pro": "deepseek-v4-pro",
    "v4-flash": "deepseek-v4-flash",

    # Mistral
    "mistral": "mistral-large-3",

    # xAI
    "grok": "grok-4.3",
    "grok-3": "grok-3",
    "grok-mini": "grok-3-mini",

    # Cohere
    "command": "command-r",
    "command+": "command-r-plus",

    # Meta
    "llama": "llama-4-maverick",
    "llama4": "llama-4-maverick",
    "llama-4": "llama-4-maverick",
    "scout": "llama-4-scout",

    # Amazon
    "nova": "nova-pro",
    "nova-lite": "nova-lite",
    "nova-micro": "nova-micro",

    # Perplexity
    "perplexity": "sonar-pro",

    # Qwen
    "qwen": "qwen-max",
    "千问": "qwen-max",

    # Moonshot/Kimi
    "kimi": "kimi-k2.6",
    "moonshot": "moonshot-v1-128k",

    # Zhipu/GLM
    "glm": "glm-5",
    "chatglm": "glm-5",
    "智谱": "glm-5",

    # MiniMax
    "minimax": "minimax-m2.7",

    # Baichuan
    "baichuan": "baichuan-m3-plus",
    "百川": "baichuan-m3-plus",

    # Yi
    "yi": "yi-large",
    "零一": "yi-large",
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


def list_providers() -> list[str]:
    """List all unique providers."""
    return sorted(set(m.provider for m in MODELS.values()))
