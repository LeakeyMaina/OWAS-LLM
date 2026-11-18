"""Compare raw model output with context-appropriate HTML encoding."""

from owasp.llm10_improper_output_handling.secure import render_summary as safe_render
from owasp.llm10_improper_output_handling.vulnerable import (
    MODEL_OUTPUT,
    render_summary as unsafe_render,
)


def main() -> None:
    """Print unsafe and escaped markup for the same model output."""
    print("Unsafe HTML: ", unsafe_render(MODEL_OUTPUT))
    print("Escaped HTML:", safe_render(MODEL_OUTPUT))


if __name__ == "__main__":
    main()
