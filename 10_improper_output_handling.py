"""LLM10: Safely render model output in the destination context (HTML here)."""

from html import escape

# A support-ticket title can be repeated by the model in an HTML dashboard.
MODEL_OUTPUT = '<img src=x onerror="alert(\'ticket\')"> Customer refund status'


def vulnerable_dashboard_card(text: str) -> str:
    # Unsafe: model output becomes active markup when inserted into a page.
    return f'<section class="summary">{text}</section>'


def safe_dashboard_card(text: str) -> str:
    # Encode for HTML text context. Use template autoescaping in a real web app.
    return f'<section class="summary">{escape(text, quote=True)}</section>'


if __name__ == "__main__":
    print("Unsafe HTML:", vulnerable_dashboard_card(MODEL_OUTPUT))
    print("Escaped HTML:", safe_dashboard_card(MODEL_OUTPUT))
