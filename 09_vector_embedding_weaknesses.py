"""LLM09: Tenant isolation must be applied before vector similarity ranking.

SQLite stands in for a vector database: the score is simple token overlap, but
the access-control mistake is the same as an unfiltered vector-store query.
"""

import sqlite3


def demo_vector_store() -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE chunks (tenant_id TEXT, text TEXT, embedding_terms TEXT)")
    db.executemany(
        "INSERT INTO chunks VALUES (?, ?, ?)",
        [
            ("team-b", "Team B acquisition roadmap: confidential", "quarterly roadmap acquisition confidential"),
            ("team-a", "Team A quarterly roadmap: publish Friday", "quarterly roadmap publish friday"),
        ],
    )
    return db


def similarity(query: str, terms: str) -> int:
    return len(set(query.lower().split()) & set(terms.lower().split()))


def vulnerable_search(db: sqlite3.Connection, query: str) -> str:
    # Ranks every tenant's vectors; authorization happens nowhere in this path.
    rows = db.execute("SELECT text, embedding_terms FROM chunks").fetchall()
    return max(rows, key=lambda row: similarity(query, row[1]))[0]


def tenant_scoped_search(db: sqlite3.Connection, tenant_id: str, query: str) -> str:
    # Filter by authenticated tenant before ranking candidate vectors.
    rows = db.execute(
        "SELECT text, embedding_terms FROM chunks WHERE tenant_id = ?", (tenant_id,)
    ).fetchall()
    if not rows:
        return "No authorized matching documents"
    return max(rows, key=lambda row: similarity(query, row[1]))[0]


if __name__ == "__main__":
    store = demo_vector_store()
    query = "quarterly roadmap acquisition"
    print("Unscoped retrieval:", vulnerable_search(store, query))
    print("Team A retrieval:  ", tenant_scoped_search(store, "team-a", query))
