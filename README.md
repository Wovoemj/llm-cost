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

- 🎯 **Accurate token counting** via tiktoken (OpenAI's official tokenizer)
- 💸 **Real pricing data** for 30+ models across 7 providers
- 📊 **Model comparison** — see which model is cheapest for your use case
- 📁 **File analysis** — estimate cost of processing entire files
- 🔗 **Aliases** — use short names like `claude-sonnet` instead of full IDs
- 📈 **Projections** — daily and monthly cost estimates
- ⚠️ **Context overflow detection** — warns when input exceeds context window
- 🖥️ **Beautiful CLI** powered by Rich
- 📤 **JSON output** for scripting and CI integration

## 🚀 Install

```bash
pip install llm-cost
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv pip install llm-cost
```

## 📖 Usage

### Estimate cost for a prompt

```bash
# Direct text
llm-cost estimate "Hello, world!" -m gpt-4o

# From file
llm-cost estimate -f ./my_prompt.txt -m claude-sonnet-4

# From stdin
echo "Summarize this article" | llm-cost estimate --stdin -m gpt-4o-mini

# With system prompt
llm-cost estimate "What is Rust?" -m gpt-4o --system "You are a senior engineer"

# Custom output ratio (output will be 2x input)
llm-cost estimate "Write a story" -m gpt-4o -r 2.0

# JSON output
llm-cost estimate "Hello" -m gpt-4o --json
```

### Compare models

```bash
# Compare popular models
llm-cost compare "Explain machine learning" -m gpt-4o,claude-sonnet-4,gemini-2.5-pro

# Default comparison (14 popular models)
llm-cost compare "Hello world"

# Top 3 cheapest
llm-cost compare "Hello" --top 3

# JSON output for scripts
llm-cost compare "Hello" --json
```

### Analyze a file

```bash
llm-cost file ./src/main.py -m gpt-4o
llm-cost file ./data/article.txt -m claude-sonnet-4 -r 0.3
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

# JSON
llm-cost list --json
```

### Show aliases

```bash
llm-cost aliases
```

## 📋 Supported Models

| Provider | Models |
|----------|--------|
| **OpenAI** | gpt-4o, gpt-4o-mini, gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, o1, o1-mini, o1-pro, o3, o3-mini, o4-mini, gpt-4-turbo, gpt-4, gpt-3.5-turbo |
| **Anthropic** | claude-opus-4, claude-sonnet-4, claude-3.5-sonnet, claude-3.5-haiku, claude-3-opus, claude-3-sonnet, claude-3-haiku |
| **Google** | gemini-2.5-pro, gemini-2.5-flash, gemini-2.0-flash, gemini-1.5-pro, gemini-1.5-flash |
| **DeepSeek** | deepseek-v3, deepseek-r1 |
| **Mistral** | mistral-large, mistral-small, codestral |
| **xAI** | grok-3, grok-3-mini |

## 🔗 Aliases

```
gpt4o           → gpt-4o
claude-opus     → claude-opus-4
claude-sonnet   → claude-sonnet-4
gemini-pro      → gemini-2.5-pro
gemini-flash    → gemini-2.5-flash
deepseek        → deepseek-v3
r1              → deepseek-r1
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
git clone https://github.com/user/llm-cost
cd llm-cost
pip install -e ".[dev]"
pytest
```

## 📄 License

MIT
