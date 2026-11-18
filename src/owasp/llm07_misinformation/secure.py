"""Check the model's structured claim against an authoritative policy record."""

from owasp.llm07_misinformation.vulnerable import DraftAnswer

POLICY_SOURCE = {"id": "refund-policy-v3", "refund_window_days": 30}


def render_verified_answer(draft: DraftAnswer) -> str:
    """Correct unsupported or conflicting claims using the trusted source."""
    if draft.citation_id != POLICY_SOURCE["id"]:
        return "I could not verify the refund deadline from an approved policy source."
    if draft.claimed_refund_days != POLICY_SOURCE["refund_window_days"]:
        return (
            f"The model claim did not match {POLICY_SOURCE['id']}. "
            f"The approved refund window is {POLICY_SOURCE['refund_window_days']} days."
        )
    # Build the final sentence from trusted fields, not free-form model text.
    return (
        f"According to {POLICY_SOURCE['id']}, refunds are available within "
        f"{POLICY_SOURCE['refund_window_days']} days."
    )


if __name__ == "__main__":
    print(render_verified_answer(DraftAnswer("90 days", 90, "refund-policy-v3")))
