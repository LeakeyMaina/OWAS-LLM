"""Compare a naive training export with the reviewed dataset gate."""

from owasp.llm05_data_model_poisoning.secure import build_reviewed_training_batch
from owasp.llm05_data_model_poisoning.vulnerable import build_training_batch


def main() -> None:
    """Print which source rows enter the vulnerable and safer batches."""
    print("Vulnerable training batch:")
    for row in build_training_batch():
        print(f"  {row['answer']} from {row['source']} (reviewed={row['reviewed']})")

    print("Reviewed training batch:")
    for row in build_reviewed_training_batch():
        print(f"  {row['answer']} from {row['source']}")


if __name__ == "__main__":
    main()
