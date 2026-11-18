"""Authorize the customer and minimize fields before building model context."""

from __future__ import annotations

import sqlite3

from owasp.llm02_sensitive_information_disclosure.data import demo_database


def build_authorized_context(
    database: sqlite3.Connection,
    authenticated_customer_id: str,
    requested_customer_id: str,
) -> dict[str, str]:
    """Return only the minimum fields for the authenticated customer."""
    if authenticated_customer_id != requested_customer_id:
        raise PermissionError("Customers may access only their own record.")

    row = database.execute(
        "SELECT plan FROM customers WHERE customer_id = ?",
        (authenticated_customer_id,),
    ).fetchone()
    if row is None:
        raise LookupError("Customer not found.")
    return {"plan": row[0]}


if __name__ == "__main__":
    print(build_authorized_context(demo_database(), "cust-101", "cust-101"))
