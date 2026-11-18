"""Unsafe context assembly that exposes every customer's record."""

from __future__ import annotations

import sqlite3

from owasp.llm02_sensitive_information_disclosure.data import demo_database


def build_context(database: sqlite3.Connection) -> list[tuple[str, str, str, float]]:
    """Return all rows, relying on the model to select the right customer."""
    return database.execute("SELECT * FROM customers").fetchall()


if __name__ == "__main__":
    print(build_context(demo_database()))
