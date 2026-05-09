# 💰 llm-cost

> Estimate LLM API costs **before** you spend a dime.

```
$ llm-cost estimate "Explain quantum computing" -m gpt-4o

╭──────── 💰 Cost Estimate ────────╮
│ Model          │ gpt-4o (OpenAI)       │
│ Input Tokens   │ 4                     │
│ Output Tokens  │ 2 (est.)              │
│ ───            │ ───                   │
│ Input Cost     │ $0.000010             │
│ Output Cost    │ $0.000020             │
│ Total Cost     │ $0.000030             │
│ ───            │ ───                   │
│ Context Window │ 128,000 tokens        │
│ Context Usage  │ 0.0% ✅               │
│ ───            │ ───                   │
│ @100 calls/day │ $0.00                 │
│ @100 calls/day │ $0.09/month           │
╰───────────────────────────────────────╯
```

## ✨ Features

- 🎯 **Heuristic token counting** — fast, no network needed (tiktoken optional)
- 💸 **111+ models** across **16 providers** — the most comprehensive pricing database
- 📊 **Model comparison** — see which model is cheapest for your use case
- 📁 **File analysis** — estimate cost of processing entire files
- 🔗 **Aliases** — use short names like `sonnet`, `4o`, `grok`
- 📈 **Projections** — daily and monthly cost estimates
- ⚠️ **Context overflow detection** — warns when input exceeds context window
- 🖥️ **Beautiful CLI** powered by Rich
- 📤 **JSON output** for scripting and CI integration
- 🌏 **Chinese provider support** — Qwen, Kimi, GLM, MiniMax, Baichuan, Yi

## 🚀 Install

```bash
pip install llm-cost
```

Or from GitHub:

```bash
pip install git+https://github.com/Wovoemj/llm-cost.git
```

## 📖 Usage

### Estimate cost for a prompt

```bash
# Direct text
llm-cost estimate "Hello, world!" -m gpt-4o

# From file
llm-cost estimate -f ./my_prompt.txt -m claude-sonnet

# From stdin
echo "Summarize this article" | llm-cost estimate --stdin -m 4o-mini

# With system prompt
llm-cost estimate "What is Rust?" -m gpt-4o --system "You are a senior engineer"

# Custom output ratio (output will be 2x input)
llm-cost estimate "Write a story" -m gpt-4o -r 2.0

# JSON output
llm-cost estimate "Hello" -m gpt-4o --json
```

### Compare models

```bash
# Compare specific models
llm-cost compare "Explain machine learning" -m gpt-4o,sonnet,gemini-pro,deepseek

# Default comparison (18 popular models)
llm-cost compare "Hello world"

# Top 5 cheapest
llm-cost compare "Hello" --top 5

# JSON output for scripts
llm-cost compare "Hello" --json
```

### Analyze a file

```bash
llm-cost file ./src/main.py -m gpt-4o
llm-cost file ./data/article.txt -m claude-sonnet -r 0.3
```

### Count tokens only

```bash
llm-cost tokens "Hello, world!"
llm-cost tokens -f ./large_file.txt
echo "pipe input" | llm-cost tokens --stdin
```

### List models

```bash
# All models
llm-cost list

# Filter by provider
llm-cost list -p anthropic
llm-cost list -p qwen

# JSON
llm-cost list --json
```

### Show aliases

```bash
llm-cost aliases
```

### Show providers

```bash
llm-cost providers
```

## 📋 Supported Providers (16)

| Provider | Country | Models | Examples |
|----------|---------|--------|----------|
| **OpenAI** | 🇺🇸 US | 27 | gpt-5.5, gpt-5.4, gpt-4.1, gpt-4o, o3, o1 |
| **Anthropic** | 🇺🇸 US | 12 | claude-opus-4.7, claude-sonnet-4.6, claude-haiku-4.5 |
| **Google** | 🇺🇸 US | 9 | gemini-3.1-pro, gemini-2.5-flash, gemini-2.0-flash |
| **Mistral** | 🇫🇷 France | 10 | magistral-medium, mistral-large-3, codestral |
| **DeepSeek** | 🇨🇳 China | 4 | deepseek-v4-pro, deepseek-v4-flash, deepseek-r1 |
| **xAI** | 🇺🇸 US | 5 | grok-4.3, grok-4.20, grok-4.1-fast |
| **Zhipu (智谱)** | 🇨🇳 China | 8 | glm-5.1, glm-5, glm-4.7-flash (free!) |
| **Moonshot (月之暗面)** | 🇨🇳 China | 6 | kimi-k2.6, kimi-k2-turbo, moonshot-v1 |
| **Qwen (通义千问)** | 🇨🇳 China | 3 | qwen-max, qwen-plus, qwen-turbo |
| **MiniMax** | 🇨🇳 China | 4 | minimax-m2.7, minimax-m2.5 |
| **Amazon** | 🇺🇸 US | 5 | nova-premier, nova-pro, nova-lite |
| **Cohere** | 🇨🇦 Canada | 4 | command-a, command-r-plus, command-r |
| **Perplexity** | 🇺🇸 US | 4 | sonar-pro, sonar-deep-research |
| **Meta** | 🇺🇸 US | 3 | llama-4-maverick, llama-4-scout |
| **Baichuan (百川)** | 🇨🇳 China | 5 | baichuan-m3-plus, baichuan4 |
| **Yi (零一万物)** | 🇨🇳 China | 2 | yi-large, yi-large-turbo |

## 🔗 Aliases

```
# OpenAI              → OpenAI                # Chinese models
4o                   → gpt-4o                 glm                  → glm-5
4o-mini              → gpt-4o-mini            chatglm              → glm-5
4.1                  → gpt-4.1                智谱                 → glm-5
5.4                  → gpt-5.4                kimi                 → kimi-k2.6
5.4-mini             → gpt-5.4-mini           moonshot             → moonshot-v1-128k

# Anthropic            # Google                qwen                 → qwen-max
sonnet               → claude-sonnet-4.6      千问                 → qwen-max
opus                 → claude-opus-4.7        minimax              → minimax-m2.7
haiku                → claude-haiku-4.5       gemini-pro           → gemini-2.5-pro
                     # DeepSeek               gemini-flash         → gemini-2.5-flash
grok                 → grok-4.3               deepseek             → deepseek-v3
grok-mini            → grok-3-mini            v4                   → deepseek-v4-pro
r1                   → deepseek-r1
```

## 🧪 CI Integration

Use `--json` output in your CI pipeline to track prompt costs:

```bash
# In your CI script
COST=$(llm-cost estimate -f prompt.txt -m gpt-4o --json | jq '.total_cost')
echo "Prompt cost: $COST"
```

## 🔧 Development

```bash
git clone https://github.com/Wovoemj/llm-cost.git
cd llm-cost
pip install -e ".[dev]"
pytest
```

## 📄 License

MIT
