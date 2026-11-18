"""Encode model text for an HTML text-node context before rendering."""

from html import escape


def render_summary(text: str) -> str:
    """Escape special HTML characters; production templates should autoescape."""
    return f'<section class="summary">{escape(text, quote=True)}</section>'


if __name__ == "__main__":
    from owasp.llm10_improper_output_handling.vulnerable import MODEL_OUTPUT

    print(render_summary(MODEL_OUTPUT))
