"""LLM02: Sensitive information disclosure from over-broad database context."""

import sqlite3


def demo_database() -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE customers (id TEXT, email TEXT, plan TEXT, balance REAL)")
    db.executemany(
        "INSERT INTO customers VALUES (?, ?, ?, ?)",
        [
            ("cust-101", "alice@example.invalid", "Basic", 12.50),
            ("cust-202", "bob@example.invalid", "Premium", 840.00),
        ],
    )
    return db


def vulnerable_context(db: sqlite3.Connection, customer_id: str) -> list[tuple]:
    # Common shortcut: dump all rows into a prompt so the model can find one.
    return db.execute("SELECT * FROM customers").fetchall()


def authorized_context(
    db: sqlite3.Connection, authenticated_customer_id: str, requested_customer_id: str
) -> dict:
    # Authorize in the application, query only that row, and minimize fields.
    if authenticated_customer_id != requested_customer_id:
        raise PermissionError("Customer may access only their own record")
    row = db.execute(
        "SELECT plan FROM customers WHERE id = ?", (authenticated_customer_id,)
    ).fetchone()
    if row is None:
        raise LookupError("Customer not found")
    return {"plan": row[0]}


if __name__ == "__main__":
    database = demo_database()
    print("Vulnerable prompt context:", vulnerable_context(database, "cust-101"))
    print("Safer prompt context:     ", authorized_context(database, "cust-101", "cust-101"))
    try:
        authorized_context(database, "cust-101", "cust-202")
    except PermissionError as error:
        print("Cross-customer request:   ", error)
