"""Unverified answer path that trusts a fluent model response and citation."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DraftAnswer:
    """Structured answer proposed by a model."""

    text: str
    claimed_refund_days: int
    citation_id: str


MODEL_DRAFT = DraftAnswer(
    text="You can request a refund within 90 days.",
    claimed_refund_days=90,
    citation_id="refund-policy-v3",
)


def render_answer(draft: DraftAnswer) -> str:
    """Display the answer without verifying the cited policy or claim."""
    return draft.text


if __name__ == "__main__":
    print(render_answer(MODEL_DRAFT))
