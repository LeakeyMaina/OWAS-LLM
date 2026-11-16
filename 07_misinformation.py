"""LLM07: Verify a generated policy answer against an authoritative source."""

from dataclasses import dataclass

POLICY_SOURCE = {"id": "refund-policy-v3", "refund_window_days": 30}


@dataclass
class DraftAnswer:
    text: str
    claimed_refund_days: int
    citation_id: str


# Representative structured model response: fluent, cited, and wrong.
MODEL_DRAFT = DraftAnswer(
    text="You can request a refund within 90 days.",
    claimed_refund_days=90,
    citation_id="refund-policy-v3",
)


def vulnerable_answer(draft: DraftAnswer) -> str:
    return draft.text  # A plausible answer and citation are accepted without checking.


def verified_answer(draft: DraftAnswer) -> str:
    source = POLICY_SOURCE
    if draft.citation_id != source["id"]:
        return "I can't verify the refund policy, so I won't state a deadline."
    if draft.claimed_refund_days != source["refund_window_days"]:
        return f"Correction from {source['id']}: refunds are available within {source['refund_window_days']} days."
    return draft.text


if __name__ == "__main__":
    print("Unverified model answer:", vulnerable_answer(MODEL_DRAFT))
    print("Checked against policy:", verified_answer(MODEL_DRAFT))
