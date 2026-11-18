"""Unsafe dispatch: model-selected destructive actions execute immediately."""

from __future__ import annotations

import json

from owasp.llm03_excessive_agency.scenario import MODEL_REQUEST
from owasp.llm03_excessive_agency.tools import AccountStore


def run(account_store: AccountStore) -> str:
    """Execute a model-requested delete without independent authorization."""
    call = json.loads(MODEL_REQUEST)
    if call["name"] == "delete_account":
        return account_store.delete(call["arguments"]["customer_id"])
    return "No action taken."


if __name__ == "__main__":
    store = AccountStore()
    print(run(store))
    print("Account state:", store.accounts)
