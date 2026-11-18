"""Compare broad prompt context with authorized, minimized context."""

from owasp.llm02_sensitive_information_disclosure.secure import build_authorized_context
from owasp.llm02_sensitive_information_disclosure.vulnerable import (
    build_context,
)
from owasp.llm02_sensitive_information_disclosure.data import demo_database


def main() -> None:
    """Show the privacy impact of putting unrelated records in model context."""
    database = demo_database()
    print("Vulnerable context:", build_context(database))
    print(
        "Authorized context:",
        build_authorized_context(database, "cust-101", "cust-101"),
    )
    try:
        build_authorized_context(database, "cust-101", "cust-202")
    except PermissionError as error:
        print("Cross-customer request blocked:", error)


if __name__ == "__main__":
    main()
