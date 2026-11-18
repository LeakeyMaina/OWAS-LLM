"""Compare a plausible but wrong answer with source verification."""

from owasp.llm07_misinformation.secure import render_verified_answer
from owasp.llm07_misinformation.vulnerable import MODEL_DRAFT, render_answer


def main() -> None:
    """Print the unverified answer and the corrected response."""
    print("Unverified answer:", render_answer(MODEL_DRAFT))
    print("Verified answer:  ", render_verified_answer(MODEL_DRAFT))


if __name__ == "__main__":
    main()
