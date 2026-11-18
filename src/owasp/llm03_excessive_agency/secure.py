"""Least-privilege account assistant with an explicit tool allowlist."""

from __future__ import annotations

import json

from owasp.llm03_excessive_agency.scenario import MODEL_REQUEST
from owasp.llm03_excessive_agency.tools import AccountStore


READ_ONLY_TOOLS = {"get_account_status"}


def run(
    account_store: AccountStore,
    authenticated_customer_id: str = "cust-101",
) -> str:
    """Reject destructive actions and bind reads to the signed-in customer."""
    call = json.loads(MODEL_REQUEST)
    tool_name = call.get("name")
    if tool_name not in READ_ONLY_TOOLS:
        return f"Blocked: {tool_name!r} is outside this assistant's permissions."

    requested_customer_id = call.get("arguments", {}).get("customer_id")
    if requested_customer_id != authenticated_customer_id:
        return "Blocked: the assistant cannot access another customer's account."
    if tool_name == "get_account_status":
        return account_store.get_status(authenticated_customer_id)
    return "Blocked: tool is not available."


def delete_with_confirmation(
    account_store: AccountStore,
    *,
    authenticated_customer_id: str,
    requested_customer_id: str,
    customer_confirmed: bool,
) -> str:
    """Delete only after the app verifies identity and obtains explicit consent."""
    if authenticated_customer_id != requested_customer_id:
        return "Blocked: account is outside the signed-in customer's scope."
    if not customer_confirmed:
        return "Blocked: explicit confirmation is required for account deletion."
    return account_store.delete(authenticated_customer_id)


if __name__ == "__main__":
    store = AccountStore()
    print(run(store))
    print(
        delete_with_confirmation(
            store,
            authenticated_customer_id="cust-101",
            requested_customer_id="cust-101",
            customer_confirmed=False,
        )
    )
