# LLM09: Vector and Embedding Weaknesses

## Scenario

A vector search ranks passages from multiple tenants and includes a poisoned, unreviewed document.

## Walk through the code

- `data.py` stores synthetic documents with a tenant ID and provenance state.
- `vulnerable.py` ranks the full collection without an authorization filter.
- `secure.py` restricts candidates to the authenticated tenant and approved sources before similarity ranking.
- `demo.py` compares the two retrieval paths.

## Security lesson

Similarity is not authorization. Apply access-control filters before ranking, keep provenance labels with indexed content, and validate that retrieval filters cannot be bypassed.
