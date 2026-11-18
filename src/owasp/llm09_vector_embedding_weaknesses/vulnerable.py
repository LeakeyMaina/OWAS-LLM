"""Unscoped semantic retrieval that returns the highest-scoring row globally."""

from owasp.llm09_vector_embedding_weaknesses.data import DOCUMENTS, Document


def search(query: str) -> Document:
    """Rank all tenants and all source states by simple term overlap."""
    query_terms = set(query.lower().split())
    return max(DOCUMENTS, key=lambda document: len(query_terms & document.terms))


if __name__ == "__main__":
    print(search("quarterly roadmap acquisition").text)
