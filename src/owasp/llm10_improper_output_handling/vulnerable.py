"""Unsafe HTML renderer that treats model output as trusted markup."""

MODEL_OUTPUT = '<img src=x onerror="alert(\'ticket\')"> Customer refund status'


def render_summary(text: str) -> str:
    """Interpolate untrusted text directly into an HTML document."""
    return f'<section class="summary">{text}</section>'


if __name__ == "__main__":
    print(render_summary(MODEL_OUTPUT))
