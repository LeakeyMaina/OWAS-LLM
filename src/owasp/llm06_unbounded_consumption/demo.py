"""Show an unlimited request and a request bounded by size and budget."""

from owasp.llm06_unbounded_consumption.secure import build_bounded_request
from owasp.llm06_unbounded_consumption.vulnerable import build_request


def main() -> None:
    """Print a normal request under both designs."""
    prompt = "Summarize this support ticket in one sentence."
    print("Vulnerable request:", build_request(prompt))
    print("Bounded request:   ", build_bounded_request(prompt, used_today=100))


if __name__ == "__main__":
    main()
