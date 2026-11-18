"""Compare immediate destructive execution with least-privilege dispatch."""

from owasp.llm03_excessive_agency import secure, vulnerable
from owasp.llm03_excessive_agency.tools import AccountStore


def main() -> None:
    """Run each path against an independent synthetic account store."""
    vulnerable_store = AccountStore()
    safe_store = AccountStore()
    print("Vulnerable app:", vulnerable.run(vulnerable_store))
    print("Vulnerable account state:", vulnerable_store.accounts)
    print("Safer app:     ", secure.run(safe_store))
    print("Safer account state:     ", safe_store.accounts)
    print(
        "Separate deletion flow:",
        secure.delete_with_confirmation(
            safe_store,
            authenticated_customer_id="cust-101",
            requested_customer_id="cust-101",
            customer_confirmed=False,
        ),
    )


if __name__ == "__main__":
    main()
