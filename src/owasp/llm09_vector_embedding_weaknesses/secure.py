"""Enforce tenant authorization and source review before ranking documents."""

from owasp.llm09_vector_embedding_weaknesses.data import DOCUMENTS, Document


def search(tenant_id: str, query: str) -> Document | None:
    """Rank only approved documents the authenticated tenant may access."""
    candidates = (
        document
        for document in DOCUMENTS
        if document.tenant_id == tenant_id and document.source_status == "approved"
    )
    query_terms = set(query.lower().split())
    return max(
        candidates,
        key=lambda document: len(query_terms & document.terms),
        default=None,
    )


if __name__ == "__main__":
    result = search("team-a", "quarterly roadmap acquisition")
    print(result.text if result else "No authorized documents")
