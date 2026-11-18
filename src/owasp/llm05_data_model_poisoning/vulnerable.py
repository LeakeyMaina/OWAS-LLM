"""Unsafe training export that admits every feedback record."""

from owasp.llm05_data_model_poisoning.data import load_feedback_rows


def build_training_batch() -> list[dict[str, str]]:
    """Include unreviewed user feedback alongside authoritative policy data."""
    return load_feedback_rows()


if __name__ == "__main__":
    for record in build_training_batch():
        print(record)
