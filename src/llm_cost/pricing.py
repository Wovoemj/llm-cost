"""Model pricing data (per 1M tokens in USD). Prices as of 2026-05.

CNY models converted at ~7.25 CNY/USD. Prices reflect the cheapest
official or well-known third-party hosting (DeepInfra, SiliconFlow, etc.).
"""

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


# fmt: off
MODELS: dict[str, ModelPricing] = {
    # ═══ OpenAI ═══════════════════════════════════════════════════════
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

    # ═══ Anthropic (Claude) ═══════════════════════════════════════════
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

    # ═══ Google Gemini ════════════════════════════════════════════════
    "gemini-3.1-pro": ModelPricing("gemini-3.1-pro", "Google", 2.00, 12.00, 1_048_576),
    "gemini-3-flash": ModelPricing("gemini-3-flash", "Google", 0.50, 3.00, 1_048_576),
    "gemini-3.1-flash-lite": ModelPricing("gemini-3.1-flash-lite", "Google", 0.25, 1.50, 1_048_576),
    "gemini-2.5-pro": ModelPricing("gemini-2.5-pro", "Google", 1.25, 10.00, 1_048_576),
    "gemini-2.5-flash": ModelPricing("gemini-2.5-flash", "Google", 0.30, 2.50, 1_048_576),
    "gemini-2.5-flash-lite": ModelPricing("gemini-2.5-flash-lite", "Google", 0.10, 0.40, 1_048_576),
    "gemini-2.0-flash": ModelPricing("gemini-2.0-flash", "Google", 0.10, 0.40, 1_048_576),
    "gemini-1.5-pro": ModelPricing("gemini-1.5-pro", "Google", 1.25, 5.00, 2_097_152),
    "gemini-1.5-flash": ModelPricing("gemini-1.5-flash", "Google", 0.075, 0.30, 1_048_576),

    # ═══ DeepSeek ═════════════════════════════════════════════════════
    "deepseek-v4-pro": ModelPricing("deepseek-v4-pro", "DeepSeek", 0.435, 0.87, 1_000_000),
    "deepseek-v4-flash": ModelPricing("deepseek-v4-flash", "DeepSeek", 0.14, 0.28, 1_000_000),
    "deepseek-v3": ModelPricing("deepseek-v3", "DeepSeek", 0.27, 1.10, 128_000),
    "deepseek-r1": ModelPricing("deepseek-r1", "DeepSeek", 0.55, 2.19, 128_000),

    # ═══ Mistral ══════════════════════════════════════════════════════
    "magistral-medium": ModelPricing("magistral-medium", "Mistral", 2.00, 5.00, 40_000),
    "mistral-large-3": ModelPricing("mistral-large-3", "Mistral", 0.50, 1.50, 262_000),
    "mistral-medium-3.1": ModelPricing("mistral-medium-3.1", "Mistral", 0.40, 2.00, 131_000),
    "mistral-medium-3": ModelPricing("mistral-medium-3", "Mistral", 0.40, 2.00, 131_000),
    "codestral": ModelPricing("codestral", "Mistral", 0.30, 0.90, 256_000),
    "mistral-small-3.2": ModelPricing("mistral-small-3.2", "Mistral", 0.075, 0.20, 131_000),
    "mistral-small-3.1": ModelPricing("mistral-small-3.1", "Mistral", 0.10, 0.30, 128_000),
    "mistral-nemo": ModelPricing("mistral-nemo", "Mistral", 0.02, 0.03, 131_000),
    "mistral-large": ModelPricing("mistral-large", "Mistral", 0.50, 1.50, 262_000),
    "mistral-small": ModelPricing("mistral-small", "Mistral", 0.10, 0.30, 128_000),
    "pixtral-large": ModelPricing("pixtral-large", "Mistral", 2.00, 6.00, 128_000),
    "pixtral-12b": ModelPricing("pixtral-12b", "Mistral", 0.10, 0.10, 128_000),

    # ═══ xAI (Grok) ══════════════════════════════════════════════════
    "grok-4.3": ModelPricing("grok-4.3", "xAI", 1.25, 2.50, 1_048_576),
    "grok-4.20": ModelPricing("grok-4.20", "xAI", 1.25, 2.50, 2_000_000),
    "grok-4.1-fast": ModelPricing("grok-4.1-fast", "xAI", 0.20, 0.50, 2_000_000),
    "grok-3": ModelPricing("grok-3", "xAI", 3.00, 15.00, 131_072),
    "grok-3-mini": ModelPricing("grok-3-mini", "xAI", 0.30, 0.50, 131_072),

    # ═══ Cohere ═══════════════════════════════════════════════════════
    "command-a": ModelPricing("command-a", "Cohere", 2.50, 10.00, 256_000),
    "command-r-plus": ModelPricing("command-r-plus", "Cohere", 2.50, 10.00, 128_000),
    "command-r": ModelPricing("command-r", "Cohere", 0.15, 0.60, 128_000),
    "command-r7b": ModelPricing("command-r7b", "Cohere", 0.037, 0.15, 128_000),

    # ═══ Meta Llama (via DeepInfra / third-party) ════════════════════
    "llama-4-maverick": ModelPricing("llama-4-maverick", "Meta", 0.15, 0.60, 1_048_576),
    "llama-4-scout": ModelPricing("llama-4-scout", "Meta", 0.08, 0.30, 328_000),
    "llama-3.3-70b": ModelPricing("llama-3.3-70b", "Meta", 0.10, 0.32, 131_000),
    "llama-3.2-90b-vision": ModelPricing("llama-3.2-90b-vision", "Meta", 0.90, 0.90, 128_000),
    "llama-3.2-11b-vision": ModelPricing("llama-3.2-11b-vision", "Meta", 0.06, 0.06, 131_000),
    "llama-3.2-3b": ModelPricing("llama-3.2-3b", "Meta", 0.03, 0.05, 80_000),
    "llama-3.2-1b": ModelPricing("llama-3.2-1b", "Meta", 0.02, 0.02, 60_000),
    "llama-3.1-405b": ModelPricing("llama-3.1-405b", "Meta", 0.90, 0.90, 131_000),
    "llama-3.1-70b": ModelPricing("llama-3.1-70b", "Meta", 0.34, 0.39, 131_000),
    "llama-3.1-8b": ModelPricing("llama-3.1-8b", "Meta", 0.02, 0.05, 16_000),
    "llama-3-70b": ModelPricing("llama-3-70b", "Meta", 0.51, 0.74, 8_000),
    "llama-3-8b": ModelPricing("llama-3-8b", "Meta", 0.03, 0.04, 8_000),

    # ═══ Amazon Nova ══════════════════════════════════════════════════
    "nova-2-lite": ModelPricing("nova-2-lite", "Amazon", 0.30, 2.50, 1_048_576),
    "nova-premier": ModelPricing("nova-premier", "Amazon", 8.00, 32.00, 200_000),
    "nova-pro": ModelPricing("nova-pro", "Amazon", 0.80, 3.20, 300_000),
    "nova-lite": ModelPricing("nova-lite", "Amazon", 0.06, 0.24, 300_000),
    "nova-micro": ModelPricing("nova-micro", "Amazon", 0.035, 0.14, 128_000),

    # ═══ Perplexity ══════════════════════════════════════════════════
    "sonar": ModelPricing("sonar", "Perplexity", 1.00, 1.00, 128_000),
    "sonar-pro": ModelPricing("sonar-pro", "Perplexity", 3.00, 15.00, 200_000),
    "sonar-reasoning-pro": ModelPricing("sonar-reasoning-pro", "Perplexity", 2.00, 8.00, 128_000),
    "sonar-deep-research": ModelPricing("sonar-deep-research", "Perplexity", 2.00, 8.00, 128_000),

    # ═══ Qwen (通义千问 / 阿里云百炼) ═══════════════════════════════
    "qwen3.6-max-preview": ModelPricing("qwen3.6-max-preview", "Qwen", 1.24, 7.45, 256_000),
    "qwen3-max": ModelPricing("qwen3-max", "Qwen", 0.34, 1.38, 128_000),
    "qwen3.5-plus": ModelPricing("qwen3.5-plus", "Qwen", 0.11, 0.66, 128_000),
    "qwen3.5-flash": ModelPricing("qwen3.5-flash", "Qwen", 0.028, 0.28, 128_000),
    "qwen3.5-397b-a17b": ModelPricing("qwen3.5-397b-a17b", "Qwen", 0.17, 0.99, 256_000),
    "qwen3.5-122b-a10b": ModelPricing("qwen3.5-122b-a10b", "Qwen", 0.11, 0.88, 256_000),
    "qwen3.5-27b": ModelPricing("qwen3.5-27b", "Qwen", 0.083, 0.66, 256_000),
    "qwen3.5-35b-a3b": ModelPricing("qwen3.5-35b-a3b", "Qwen", 0.055, 0.44, 256_000),
    "qwen3-235b-a22b": ModelPricing("qwen3-235b-a22b", "Qwen", 0.28, 1.10, 128_000),
    "qwen3-32b": ModelPricing("qwen3-32b", "Qwen", 0.28, 1.10, 128_000),
    "qwen3-30b-a3b": ModelPricing("qwen3-30b-a3b", "Qwen", 0.10, 0.41, 128_000),
    "qwen3-14b": ModelPricing("qwen3-14b", "Qwen", 0.14, 0.55, 128_000),
    "qwen3-8b": ModelPricing("qwen3-8b", "Qwen", 0.069, 0.28, 128_000),
    "qwen3-4b": ModelPricing("qwen3-4b", "Qwen", 0.041, 0.17, 128_000),
    "qwen3-1.7b": ModelPricing("qwen3-1.7b", "Qwen", 0.041, 0.17, 128_000),
    "qwen3-coder-480b-a35b": ModelPricing("qwen3-coder-480b-a35b", "Qwen", 0.83, 3.31, 128_000),
    "qwen3-coder-30b-a3b": ModelPricing("qwen3-coder-30b-a3b", "Qwen", 0.21, 0.83, 128_000),
    "qwen2.5-72b": ModelPricing("qwen2.5-72b", "Qwen", 0.55, 1.66, 128_000),
    "qwen2.5-32b": ModelPricing("qwen2.5-32b", "Qwen", 0.28, 0.83, 128_000),
    "qwen2.5-14b": ModelPricing("qwen2.5-14b", "Qwen", 0.14, 0.55, 128_000),
    "qwen2.5-7b": ModelPricing("qwen2.5-7b", "Qwen", 0.175, 0.70, 128_000),
    "qwq-32b": ModelPricing("qwq-32b", "Qwen", 0.28, 2.76, 128_000),
    "qwen-max": ModelPricing("qwen-max", "Qwen", 1.04, 4.16, 32_000),
    "qwen-plus": ModelPricing("qwen-plus", "Qwen", 0.26, 0.78, 131_000),
    "qwen-turbo": ModelPricing("qwen-turbo", "Qwen", 0.10, 0.30, 131_000),

    # ═══ Moonshot / Kimi (月之暗面) ══════════════════════════════════
    "kimi-k2.6": ModelPricing("kimi-k2.6", "Moonshot", 0.60, 2.50, 262_000),
    "kimi-k2-thinking": ModelPricing("kimi-k2-thinking", "Moonshot", 0.60, 2.50, 262_000),
    "kimi-k2-turbo": ModelPricing("kimi-k2-turbo", "Moonshot", 1.15, 8.00, 262_000),
    "moonshot-v1-128k": ModelPricing("moonshot-v1-128k", "Moonshot", 2.00, 5.00, 131_000),
    "moonshot-v1-32k": ModelPricing("moonshot-v1-32k", "Moonshot", 1.00, 3.00, 33_000),
    "moonshot-v1-8k": ModelPricing("moonshot-v1-8k", "Moonshot", 0.20, 2.00, 8_000),

    # ═══ Zhipu / GLM (智谱清言) ══════════════════════════════════════
    "glm-5.1": ModelPricing("glm-5.1", "Zhipu", 1.40, 4.40, 203_000),
    "glm-5": ModelPricing("glm-5", "Zhipu", 1.00, 3.20, 203_000),
    "glm-5-turbo": ModelPricing("glm-5-turbo", "Zhipu", 1.20, 4.00, 203_000),
    "glm-5v-turbo": ModelPricing("glm-5v-turbo", "Zhipu", 1.20, 4.00, 203_000),
    "glm-4.7": ModelPricing("glm-4.7", "Zhipu", 0.60, 2.20, 205_000),
    "glm-4.7-flashx": ModelPricing("glm-4.7-flashx", "Zhipu", 0.07, 0.40, 205_000),
    "glm-4.7-flash": ModelPricing("glm-4.7-flash", "Zhipu", 0.0, 0.0, 203_000),
    "glm-4.6": ModelPricing("glm-4.6", "Zhipu", 0.60, 2.20, 205_000),
    "glm-4.6v": ModelPricing("glm-4.6v", "Zhipu", 0.30, 0.90, 131_000),
    "glm-4.6v-flash": ModelPricing("glm-4.6v-flash", "Zhipu", 0.0, 0.0, 131_000),
    "glm-4.5": ModelPricing("glm-4.5", "Zhipu", 0.60, 2.20, 131_000),
    "glm-4.5-x": ModelPricing("glm-4.5-x", "Zhipu", 2.20, 8.90, 205_000),
    "glm-4.5-air": ModelPricing("glm-4.5-air", "Zhipu", 0.20, 1.10, 131_000),
    "glm-4.5-airx": ModelPricing("glm-4.5-airx", "Zhipu", 1.10, 4.50, 205_000),
    "glm-4.5-flash": ModelPricing("glm-4.5-flash", "Zhipu", 0.0, 0.0, 205_000),
    "glm-4.5v": ModelPricing("glm-4.5v", "Zhipu", 0.60, 1.80, 205_000),
    "glm-4-32b": ModelPricing("glm-4-32b", "Zhipu", 0.10, 0.10, 128_000),
    "glm-ocr": ModelPricing("glm-ocr", "Zhipu", 0.03, 0.03, 128_000),

    # ═══ Baidu ERNIE (百度文心) ═══════════════════════════════════════
    "ernie-5.1": ModelPricing("ernie-5.1", "Baidu", 0.55, 2.48, 128_000),
    "ernie-5.0-thinking": ModelPricing("ernie-5.0-thinking", "Baidu", 0.83, 3.31, 128_000),
    "ernie-x1.1": ModelPricing("ernie-x1.1", "Baidu", 0.14, 0.55, 128_000),
    "ernie-x1-turbo": ModelPricing("ernie-x1-turbo", "Baidu", 0.14, 0.55, 32_000),
    "ernie-4.5-turbo": ModelPricing("ernie-4.5-turbo", "Baidu", 0.11, 0.44, 128_000),
    "ernie-4.5-turbo-vl": ModelPricing("ernie-4.5-turbo-vl", "Baidu", 0.41, 1.24, 32_000),
    "ernie-4.5": ModelPricing("ernie-4.5", "Baidu", 0.55, 2.21, 8_000),
    "ernie-4.5-0.3b": ModelPricing("ernie-4.5-0.3b", "Baidu", 0.014, 0.055, 8_000),
    "ernie-4.5-300b": ModelPricing("ernie-4.5-300b", "Baidu", 0.28, 0.90, 123_000),
    "ernie-4.5-21b": ModelPricing("ernie-4.5-21b", "Baidu", 0.07, 0.28, 120_000),
    "ernie-4.5-21b-thinking": ModelPricing("ernie-4.5-21b-thinking", "Baidu", 0.07, 0.28, 131_000),
    "ernie-4.5-vl-424b": ModelPricing("ernie-4.5-vl-424b", "Baidu", 0.42, 1.25, 123_000),
    "ernie-speed-pro": ModelPricing("ernie-speed-pro", "Baidu", 0.041, 0.083, 128_000),
    "ernie-lite-pro": ModelPricing("ernie-lite-pro", "Baidu", 0.028, 0.055, 128_000),

    # ═══ ByteDance Doubao (字节豆包) ══════════════════════════════════
    "doubao-seed-2.0-pro": ModelPricing("doubao-seed-2.0-pro", "ByteDance", 0.44, 2.21, 128_000),
    "doubao-seed-2.0-lite": ModelPricing("doubao-seed-2.0-lite", "ByteDance", 0.083, 0.50, 128_000),
    "doubao-seed-2.0-mini": ModelPricing("doubao-seed-2.0-mini", "ByteDance", 0.028, 0.28, 128_000),
    "doubao-seed-code": ModelPricing("doubao-seed-code", "ByteDance", 0.17, 1.10, 128_000),

    # ═══ Tencent Hunyuan (腾讯混元) ══════════════════════════════════
    "hunyuan-2.0-think": ModelPricing("hunyuan-2.0-think", "Tencent", 0.55, 2.19, 128_000),
    "hunyuan-2.0-instruct": ModelPricing("hunyuan-2.0-instruct", "Tencent", 0.44, 1.10, 128_000),
    "hunyuan-t1": ModelPricing("hunyuan-t1", "Tencent", 0.14, 0.55, 128_000),
    "hunyuan-turbos": ModelPricing("hunyuan-turbos", "Tencent", 0.11, 0.28, 128_000),
    "hunyuan-a13b": ModelPricing("hunyuan-a13b", "Tencent", 0.069, 0.28, 131_000),
    "hunyuan-large-role": ModelPricing("hunyuan-large-role", "Tencent", 0.33, 1.32, 128_000),
    "hunyuan-translation": ModelPricing("hunyuan-translation", "Tencent", 0.17, 0.50, 128_000),
    "hunyuan-translation-lite": ModelPricing("hunyuan-translation-lite", "Tencent", 0.14, 0.41, 128_000),
    "hunyuan-lite": ModelPricing("hunyuan-lite", "Tencent", 0.0, 0.0, 250_000),
    "hunyuan-vision-1.5": ModelPricing("hunyuan-vision-1.5", "Tencent", 0.41, 1.24, 128_000),
    "hunyuan-turbos-vision": ModelPricing("hunyuan-turbos-vision", "Tencent", 0.41, 1.24, 128_000),
    "hunyuan-t1-vision": ModelPricing("hunyuan-t1-vision", "Tencent", 0.41, 1.24, 128_000),

    # ═══ StepFun / 阶跃星辰 ══════════════════════════════════════════
    "step-3": ModelPricing("step-3", "StepFun", 0.55, 1.38, 256_000),
    "step-3.5-flash": ModelPricing("step-3.5-flash", "StepFun", 0.10, 0.30, 256_000),

    # ═══ iFlytek Spark (讯飞星火) ════════════════════════════════════
    # Note: iFlytek uses non-standard token-package pricing.
    # Prices below are approximate per-token rates.
    "spark-4.0-ultra": ModelPricing("spark-4.0-ultra", "iFlytek", 2.07, 2.07, 128_000),
    "spark-max": ModelPricing("spark-max", "iFlytek", 1.03, 1.03, 128_000),
    "spark-pro": ModelPricing("spark-pro", "iFlytek", 0.34, 0.34, 128_000),
    "spark-lite": ModelPricing("spark-lite", "iFlytek", 0.0, 0.0, 8_000),
    "spark-x1": ModelPricing("spark-x1", "iFlytek", 1.03, 1.03, 128_000),

    # ═══ MiniMax ══════════════════════════════════════════════════════
    "minimax-m2.7": ModelPricing("minimax-m2.7", "MiniMax", 0.30, 1.20, 204_000),
    "minimax-m2.7-highspeed": ModelPricing("minimax-m2.7-highspeed", "MiniMax", 0.60, 2.40, 204_000),
    "minimax-m2.5": ModelPricing("minimax-m2.5", "MiniMax", 0.30, 1.20, 1_048_576),
    "minimax-m2.5-highspeed": ModelPricing("minimax-m2.5-highspeed", "MiniMax", 0.60, 2.40, 1_048_576),
    "minimax-m1": ModelPricing("minimax-m1", "MiniMax", 0.40, 1.60, 1_048_576),

    # ═══ Baichuan (百川智能) ══════════════════════════════════════════
    "baichuan-m3-plus": ModelPricing("baichuan-m3-plus", "Baichuan", 0.69, 1.24, 32_000),
    "baichuan-m3": ModelPricing("baichuan-m3", "Baichuan", 1.38, 4.14, 32_000),
    "baichuan-m2-plus": ModelPricing("baichuan-m2-plus", "Baichuan", 1.38, 4.14, 32_000),
    "baichuan-m2": ModelPricing("baichuan-m2", "Baichuan", 0.28, 2.76, 32_000),
    "baichuan4-turbo": ModelPricing("baichuan4-turbo", "Baichuan", 2.07, 2.07, 32_000),
    "baichuan4-air": ModelPricing("baichuan4-air", "Baichuan", 0.14, 0.14, 32_000),
    "baichuan4": ModelPricing("baichuan4", "Baichuan", 13.80, 13.80, 32_000),
    "baichuan3-turbo": ModelPricing("baichuan3-turbo", "Baichuan", 1.66, 1.66, 32_000),
    "baichuan3-turbo-128k": ModelPricing("baichuan3-turbo-128k", "Baichuan", 3.31, 3.31, 128_000),
    "baichuan2-turbo": ModelPricing("baichuan2-turbo", "Baichuan", 1.10, 1.10, 32_000),

    # ═══ Yi (零一万物) ════════════════════════════════════════════════
    "yi-large": ModelPricing("yi-large", "Yi", 3.00, 3.00, 32_000),
    "yi-large-turbo": ModelPricing("yi-large-turbo", "Yi", 0.60, 0.60, 32_000),
    "yi-medium": ModelPricing("yi-medium", "Yi", 0.30, 0.30, 16_000),
    "yi-spark": ModelPricing("yi-spark", "Yi", 0.10, 0.10, 16_000),

    # ═══ SiliconFlow (硅基流动 — 聚合平台) ═══════════════════════════
    "sf-deepseek-v4-flash": ModelPricing("sf-deepseek-v4-flash", "SiliconFlow", 0.14, 0.28, 1_049_000),
    "sf-deepseek-v4-pro": ModelPricing("sf-deepseek-v4-pro", "SiliconFlow", 1.74, 3.48, 1_049_000),
    "sf-deepseek-v3.2": ModelPricing("sf-deepseek-v3.2", "SiliconFlow", 0.27, 0.42, 164_000),
    "sf-kimi-k2.5": ModelPricing("sf-kimi-k2.5", "SiliconFlow", 0.23, 3.00, 262_000),
    "sf-hunyuan-a13b": ModelPricing("sf-hunyuan-a13b", "SiliconFlow", 0.14, 0.57, 131_000),
    "sf-qwen3-vl-32b": ModelPricing("sf-qwen3-vl-32b", "SiliconFlow", 0.20, 0.60, 262_000),
    "sf-qwen3-vl-8b": ModelPricing("sf-qwen3-vl-8b", "SiliconFlow", 0.18, 0.68, 262_000),
}
# fmt: on


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
    "mistral-medium": "mistral-medium-3.1",
    # xAI
    "grok": "grok-4.3",
    "grok-mini": "grok-3-mini",
    # Cohere
    "command": "command-r",
    "command+": "command-r-plus",
    # Meta
    "llama": "llama-4-maverick",
    "llama4": "llama-4-maverick",
    "llama-4": "llama-4-maverick",
    "scout": "llama-4-scout",
    "llama-3.3": "llama-3.3-70b",
    "llama-3.1-405b": "llama-3.1-405b",
    "llama-3.1-70b": "llama-3.1-70b",
    "llama-3.1-8b": "llama-3.1-8b",
    # Amazon
    "nova": "nova-pro",
    # Perplexity
    "perplexity": "sonar-pro",
    # Qwen
    "qwen": "qwen3-max",
    "qwen3": "qwen3-max",
    "qwen3.5": "qwen3.5-plus",
    "qwen3-coder": "qwen3-coder-480b-a35b",
    "qwq": "qwq-32b",
    "千问": "qwen3-max",
    # Moonshot/Kimi
    "kimi": "kimi-k2.6",
    "moonshot": "moonshot-v1-128k",
    # Zhipu/GLM
    "glm": "glm-5",
    "chatglm": "glm-5",
    "智谱": "glm-5",
    # Baidu ERNIE
    "ernie": "ernie-4.5-turbo",
    "ernie4.5": "ernie-4.5-turbo",
    "ernie5": "ernie-5.1",
    "百度": "ernie-4.5-turbo",
    "文心": "ernie-4.5-turbo",
    # ByteDance Doubao
    "doubao": "doubao-seed-2.0-pro",
    "豆包": "doubao-seed-2.0-pro",
    # Tencent Hunyuan
    "hunyuan": "hunyuan-2.0-instruct",
    "混元": "hunyuan-2.0-instruct",
    # StepFun
    "step": "step-3",
    "阶跃": "step-3.5-flash",
    # iFlytek
    "spark": "spark-4.0-ultra",
    "星火": "spark-4.0-ultra",
    # MiniMax
    "minimax": "minimax-m2.7",
    # Baichuan
    "baichuan": "baichuan-m3-plus",
    "百川": "baichuan-m3-plus",
    # Yi
    "yi": "yi-large",
    "零一": "yi-large",
    # SiliconFlow
    "sf": "sf-deepseek-v4-flash",
    "硅基": "sf-deepseek-v4-flash",
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
