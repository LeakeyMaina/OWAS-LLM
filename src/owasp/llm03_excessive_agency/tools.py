"""Tools for a local account-management example."""

from __future__ import annotations

from dataclasses import dataclass, field

from langchain.tools import tool

AUTHENTICATED_CUSTOMER_ID = "cust-101"


@dataclass(slots=True)
class AccountStore:
    """In-memory account store with synthetic records."""

    accounts: dict[str, str] = field(default_factory=lambda: {"cust-101": "active"})

    def get_status(self, customer_id: str) -> str:
        """Read an account status without changing state."""
        return self.accounts.get(customer_id, "not found")

    def delete(self, customer_id: str) -> str:
        """Delete an account from the local demonstration store."""
        if self.accounts.pop(customer_id, None) is None:
            return "Account not found."
        return f"Demo account {customer_id} deleted."


ACCOUNT_STORE = AccountStore()


@tool
def get_account_status(customer_id: str) -> str:
    """Read the status of a support account.

    Args:
        customer_id: Account identifier to look up.
    """
    if customer_id != AUTHENTICATED_CUSTOMER_ID:
        return "Access denied: account is outside the signed-in customer's scope."
    return ACCOUNT_STORE.get_status(AUTHENTICATED_CUSTOMER_ID)


@tool
def delete_account(customer_id: str) -> str:
    """Delete a support account from the demo store.

    Args:
        customer_id: Account identifier to delete.
    """
    return ACCOUNT_STORE.delete(customer_id)
