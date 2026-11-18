"""Admit only reviewed records with expected provenance and integrity status."""

from owasp.llm05_data_model_poisoning.data import load_feedback_rows


def build_reviewed_training_batch() -> list[dict[str, str]]:
    """Fail closed when provenance, review, or integrity metadata is missing."""
    return [
        row
        for row in load_feedback_rows()
        if row.get("source") == "approved_policy"
        and row.get("reviewed") == "true"
        and row.get("integrity_verified") == "true"
    ]


if __name__ == "__main__":
    for record in build_reviewed_training_batch():
        print(record)
