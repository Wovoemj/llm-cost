"""Tests for llm-cost."""

from llm_cost.pricing import get_model, list_models, MODELS, ALIASES
from llm_cost.tokens import count_tokens
from llm_cost.cost import estimate_cost, compare_models


class TestPricing:
    def test_get_model_gpt4o(self):
        m = get_model("gpt-4o")
        assert m.name == "gpt-4o"
        assert m.provider == "OpenAI"
        assert m.input_price == 2.50

    def test_get_model_alias(self):
        m = get_model("claude-sonnet")
        assert m.name == "claude-sonnet-4"

    def test_get_model_case_insensitive(self):
        m = get_model("GPT-4O")
        assert m.name == "gpt-4o"

    def test_get_model_unknown(self):
        try:
            get_model("nonexistent-model")
            assert False, "Should have raised KeyError"
        except KeyError as e:
            assert "nonexistent-model" in str(e)

    def test_list_models_all(self):
        models = list_models()
        assert len(models) >= 25

    def test_list_models_by_provider(self):
        models = list_models("Anthropic")
        assert all(m.provider == "Anthropic" for m in models)
        assert len(models) >= 4


class TestTokens:
    def test_count_simple(self):
        count = count_tokens("Hello, world!")
        assert 2 <= count <= 5

    def test_count_empty(self):
        count = count_tokens("")
        assert count == 0

    def test_count_long(self):
        text = "word " * 1000
        count = count_tokens(text)
        assert count > 900


class TestCost:
    def test_estimate_basic(self):
        result = estimate_cost("Hello, world!", "gpt-4o")
        assert result.model == "gpt-4o"
        assert result.input_tokens > 0
        assert result.output_tokens > 0
        assert result.total_cost > 0

    def test_estimate_with_system(self):
        result = estimate_cost("Hello", "gpt-4o", system_prompt="You are a helpful assistant.")
        assert result.input_tokens > count_tokens("Hello")

    def test_estimate_different_models(self):
        r1 = estimate_cost("Hello, world!", "gpt-4o")
        r2 = estimate_cost("Hello, world!", "gpt-4o-mini")
        # mini is cheaper
        assert r2.total_cost < r1.total_cost

    def test_compare_models(self):
        results = compare_models("Hello", ["gpt-4o", "gpt-4o-mini", "claude-sonnet-4"])
        assert len(results) == 3
        # Should be sorted by cost
        assert results[0].total_cost <= results[-1].total_cost

    def test_context_overflow(self):
        # Generate a very long text that exceeds context
        long_text = "word " * 200_000  # ~200k tokens
        result = estimate_cost(long_text, "gpt-3.5-turbo")
        assert not result.fits_context

    def test_cost_display_small(self):
        result = estimate_cost("Hi", "gpt-4o-mini")
        assert result.total_cost_display.startswith("$")
        assert "0.00" in result.total_cost_display

    def test_monthly_projection(self):
        result = estimate_cost("Hello", "gpt-4o")
        monthly = result.to_monthly(100)
        assert monthly > 0


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
