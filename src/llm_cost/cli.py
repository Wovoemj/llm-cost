"""CLI entry point using Click + Rich."""

from __future__ import annotations
import os
import sys
import json
import select
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

from . import __version__
from .cost import estimate_cost, compare_models, estimate_file_cost
from .pricing import get_model, list_models, MODELS, ALIASES
from .tokens import count_tokens

console = Console()


def _has_stdin_data() -> bool:
    """Check if stdin has data waiting (piped input)."""
    try:
        if sys.stdin.isatty():
            return False
        # Non-tty: check if there's data ready
        r, _, _ = select.select([sys.stdin], [], [], 0)
        return bool(r)
    except Exception:
        return False


def _get_input(text: str | None, file: str | None, stdin: bool) -> str:
    """Resolve input text from text arg, file, or stdin."""
    if file:
        with open(file, "r", encoding="utf-8") as f:
            return f.read()
    if stdin:
        return sys.stdin.read()
    if text:
        return text
    return ""


@click.group()
@click.version_option(version=__version__, prog_name="llm-cost")
def cli():
    """💰 llm-cost — Estimate LLM API costs before you spend a dime."""
    pass


@cli.command()
@click.argument("text", required=False)
@click.option("-m", "--model", default="gpt-4o", help="Model name (e.g. gpt-4o, claude-sonnet-4)")
@click.option("-f", "--file", "filepath", type=click.Path(exists=True), help="Read input from file")
@click.option("--stdin", is_flag=True, help="Read input from stdin")
@click.option("-r", "--ratio", default=0.5, type=float, help="Output/input token ratio (default: 0.5)")
@click.option("--system", default=None, help="System prompt to include in token count")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def estimate(text, model, filepath, stdin, ratio, system, as_json):
    """Estimate cost for a prompt.

    \b
    Examples:
      llm-cost estimate "Hello world" -m gpt-4o
      llm-cost estimate -f ./prompt.txt -m claude-sonnet-4
      echo "Hello" | llm-cost estimate --stdin -m gpt-4o-mini
    """
    input_text = _get_input(text, filepath, stdin)
    if not input_text:
        console.print("[red]Error:[/] No input text. Pass text, use -f, or pipe via stdin.")
        raise SystemExit(1)

    result = estimate_cost(input_text, model, ratio, system_prompt=system)

    if as_json:
        click.echo(json.dumps({
            "model": result.model,
            "provider": result.provider,
            "input_tokens": result.input_tokens,
            "output_tokens": result.output_tokens,
            "input_cost": result.input_cost,
            "output_cost": result.output_cost,
            "total_cost": result.total_cost,
            "context_window": result.context_window,
            "context_usage_pct": result.context_usage_pct,
        }, indent=2))
        return

    _print_result(result)


def _print_result(result):
    """Pretty-print a single cost result."""
    fits = "✅" if result.fits_context else "⚠️ OVERFLOW"

    table = Table(
        box=box.ROUNDED,
        show_header=False,
        padding=(0, 2),
        border_style="bright_blue",
    )
    table.add_column("Key", style="bold")
    table.add_column("Value")

    table.add_row("Model", f"{result.model} ({result.provider})")
    table.add_row("Input Tokens", f"{result.input_tokens:,}")
    table.add_row("Output Tokens", f"{result.output_tokens:,} (est.)")
    table.add_row("───", "───")
    table.add_row("Input Cost", f"${result.input_cost:.6f}")
    table.add_row("Output Cost", f"${result.output_cost:.6f}")
    table.add_row("Total Cost", f"[bold green]{result.total_cost_display}[/]")
    table.add_row("───", "───")
    table.add_row("Context Window", f"{result.context_window:,} tokens")
    table.add_row("Context Usage", f"{result.context_usage_pct}% {fits}")
    table.add_row("───", "───")
    table.add_row("@100 calls/day", f"${result.to_daily(100):.2f}")
    table.add_row("@100/day monthly", f"${result.to_monthly(100):.2f}/month")

    console.print(Panel(table, title="💰 Cost Estimate", border_style="green"))


@cli.command()
@click.argument("text", required=False)
@click.option("-m", "--models", default=None, help="Comma-separated models (default: popular set)")
@click.option("-f", "--file", "filepath", type=click.Path(exists=True), help="Read input from file")
@click.option("--stdin", is_flag=True, help="Read input from stdin")
@click.option("-r", "--ratio", default=0.5, type=float, help="Output/input token ratio")
@click.option("--system", default=None, help="System prompt")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
@click.option("-n", "--top", default=None, type=int, help="Show only top N cheapest")
def compare(text, models, filepath, stdin, ratio, system, as_json, top):
    """Compare cost across multiple models.

    \b
    Examples:
      llm-cost compare "Explain ML"
      llm-cost compare "Hello" -m gpt-4o,claude-sonnet-4,gemini-2.5-pro --top 3
    """
    input_text = _get_input(text, filepath, stdin)
    if not input_text:
        console.print("[red]Error:[/] No input text.")
        raise SystemExit(1)

    if models:
        model_list = [m.strip() for m in models.split(",")]
    else:
        model_list = [
            "gpt-4o", "gpt-4o-mini", "gpt-4.1", "gpt-4.1-mini",
            "claude-sonnet-4", "claude-3.5-haiku",
            "gemini-2.5-pro", "gemini-2.5-flash",
            "deepseek-v3", "deepseek-r1",
            "mistral-large", "mistral-small",
            "grok-3", "grok-3-mini",
        ]

    results = compare_models(input_text, model_list, ratio, system_prompt=system)
    if top:
        results = results[:top]

    if as_json:
        data = [{
            "model": r.model,
            "provider": r.provider,
            "input_tokens": r.input_tokens,
            "output_tokens": r.output_tokens,
            "total_cost": r.total_cost,
            "context_usage_pct": r.context_usage_pct,
        } for r in results]
        click.echo(json.dumps(data, indent=2))
        return

    _print_comparison(results)


def _print_comparison(results):
    """Pretty-print comparison table."""
    table = Table(
        title="💰 Model Cost Comparison",
        box=box.ROUNDED,
        border_style="bright_blue",
    )
    table.add_column("#", style="dim", width=3)
    table.add_column("Model", style="bold")
    table.add_column("Provider")
    table.add_column("Input $", justify="right")
    table.add_column("Output $", justify="right")
    table.add_column("Total $", justify="right", style="bold green")
    table.add_column("Ctx %", justify="right")
    table.add_column("Monthly*", justify="right", style="yellow")

    for i, r in enumerate(results, 1):
        ctx_style = "green" if r.fits_context else "red"
        table.add_row(
            str(i),
            r.model,
            r.provider,
            f"${r.input_cost:.6f}",
            f"${r.output_cost:.6f}",
            f"${r.total_cost:.4f}",
            f"[{ctx_style}]{r.context_usage_pct}%[/]",
            f"${r.to_monthly(100):.2f}",
        )

    console.print()
    console.print(table)
    console.print("[dim]* Monthly = 100 calls/day × 30 days[/]")
    console.print()


@cli.command()
@click.argument("filepath", type=click.Path(exists=True))
@click.option("-m", "--model", default="gpt-4o", help="Model name")
@click.option("-r", "--ratio", default=0.5, type=float, help="Output/input token ratio")
@click.option("--system", default=None, help="System prompt")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def file(filepath, model, ratio, system, as_json):
    """Estimate cost for processing a file.

    \b
    Examples:
      llm-cost file ./src/main.py -m gpt-4o
      llm-cost file ./article.txt -m claude-sonnet-4 -r 0.3
    """
    result = estimate_file_cost(filepath, model, ratio, system_prompt=system)

    if as_json:
        click.echo(json.dumps({
            "file": filepath,
            "model": result.model,
            "input_tokens": result.input_tokens,
            "total_cost": result.total_cost,
        }, indent=2))
        return

    _print_result(result)


@cli.command(name="list")
@click.option("-p", "--provider", default=None, help="Filter by provider")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def list_cmd(provider, as_json):
    """List all supported models and their pricing."""
    models = list_models(provider)

    if as_json:
        data = [{
            "name": m.name,
            "provider": m.provider,
            "input_price": m.input_price,
            "output_price": m.output_price,
            "context_window": m.context_window,
        } for m in models]
        click.echo(json.dumps(data, indent=2))
        return

    table = Table(
        title="📋 Supported Models",
        box=box.ROUNDED,
        border_style="bright_blue",
    )
    table.add_column("Model", style="bold")
    table.add_column("Provider")
    table.add_column("Input $/1M", justify="right")
    table.add_column("Output $/1M", justify="right")
    table.add_column("Context", justify="right")

    current_provider = None
    for m in models:
        if current_provider and m.provider != current_provider:
            table.add_row("", "", "", "", "")
        current_provider = m.provider
        table.add_row(
            m.name,
            m.provider,
            f"${m.input_price:.2f}",
            f"${m.output_price:.2f}",
            f"{m.context_window:,}",
        )

    console.print()
    console.print(table)
    console.print()


@cli.command()
@click.argument("text", required=False)
@click.option("-f", "--file", "filepath", type=click.Path(exists=True), help="Read input from file")
@click.option("--stdin", is_flag=True, help="Read input from stdin")
def tokens(text, filepath, stdin):
    """Count tokens in text (no cost calculation).

    \b
    Examples:
      llm-cost tokens "Hello, world!"
      llm-cost tokens -f ./large_file.txt
    """
    input_text = _get_input(text, filepath, stdin)
    if not input_text:
        console.print("[red]Error:[/] No input text.")
        raise SystemExit(1)

    count = count_tokens(input_text)
    word_count = len(input_text.split())
    char_count = len(input_text)

    console.print()
    console.print(f"  [bold]Tokens:[/]  {count:,}")
    console.print(f"  [bold]Words:[/]   {word_count:,}")
    console.print(f"  [bold]Chars:[/]   {char_count:,}")
    console.print()


@cli.command()
def aliases():
    """Show model aliases/shortcuts."""
    table = Table(
        title="🔗 Model Aliases",
        box=box.ROUNDED,
        border_style="bright_blue",
    )
    table.add_column("Alias", style="bold cyan")
    table.add_column("→", style="dim")
    table.add_column("Model", style="bold")

    for alias, model in sorted(ALIASES.items()):
        table.add_row(alias, "→", model)

    console.print()
    console.print(table)
    console.print()


if __name__ == "__main__":
    cli()
