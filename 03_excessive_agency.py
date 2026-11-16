"""LLM03: Excessive agency in an account-support agent."""

import json
import sqlite3

MODEL_REQUEST = '{"name":"delete_account","arguments":{"customer_id":"cust-101"}}'


def demo_database() -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE accounts (customer_id TEXT PRIMARY KEY, status TEXT)")
    db.execute("INSERT INTO accounts VALUES (?, ?)", ("cust-101", "active"))
    return db


def vulnerable(db: sqlite3.Connection) -> str:
    call = json.loads(MODEL_REQUEST)
    # The model can invoke any registered tool; the app executes without review.
    if call["name"] == "delete_account":
        db.execute("DELETE FROM accounts WHERE customer_id = ?", (call["arguments"]["customer_id"],))
        db.commit()
    return f"Rows remaining: {db.execute('SELECT COUNT(*) FROM accounts').fetchone()[0]}"


def safer(db: sqlite3.Connection) -> str:
    call = json.loads(MODEL_REQUEST)
    # This assistant may check status only. Deletion requires a separate verified flow.
    if call.get("name") != "get_account_status":
        return "Blocked: account changes are outside this assistant's permissions"
    customer_id = call.get("arguments", {}).get("customer_id")
    row = db.execute("SELECT status FROM accounts WHERE customer_id = ?", (customer_id,)).fetchone()
    return row[0] if row else "Account not found"


if __name__ == "__main__":
    unsafe_db = demo_database()
    safe_db = demo_database()
    print("Vulnerable:", vulnerable(unsafe_db))
    print("Safer:     ", safer(safe_db))
