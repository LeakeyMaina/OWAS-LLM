"""Show how global retrieval can leak across tenants or surface unreviewed text."""

from owasp.llm09_vector_embedding_weaknesses.secure import search as secure_search
from owasp.llm09_vector_embedding_weaknesses.vulnerable import search as unsafe_search


def main() -> None:
    """Search the same query globally and within Team A's authorized corpus."""
    query = "quarterly roadmap acquisition"
    print("Unscoped retrieval:", unsafe_search(query).text)
    result = secure_search("team-a", query)
    print("Team A retrieval:  ", result.text if result else "No authorized documents")


if __name__ == "__main__":
    main()
