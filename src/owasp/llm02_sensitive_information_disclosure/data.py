"""Create the synthetic customer database shared by both LLM02 paths."""

from __future__ import annotations

import sqlite3


def demo_database() -> sqlite3.Connection:
    """Create an in-memory database with fake customer records."""
    database = sqlite3.connect(":memory:")
    database.execute(
        "CREATE TABLE customers "
        "(customer_id TEXT PRIMARY KEY, email TEXT, plan TEXT, balance REAL)"
    )
    database.executemany(
        "INSERT INTO customers VALUES (?, ?, ?, ?)",
        [
            ("cust-101", "alice@example.invalid", "Basic", 12.50),
            ("cust-202", "bob@example.invalid", "Premium", 840.00),
        ],
    )
    return database
