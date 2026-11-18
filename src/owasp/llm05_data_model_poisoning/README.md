# LLM05: Data and Model Poisoning

## Scenario

Public support feedback is exported into a fine-tuning dataset. One unchecked row teaches an incorrect refund policy.

## Walk through the code

- `data.py` parses a CSV fixture and retains source, review, and integrity metadata.
- `vulnerable.py` admits every row.
- `secure.py` includes a row only when it came from the approved policy source, passed human review, and passed integrity verification.
- `demo.py` compares the resulting training batches.

## Security lesson

Keep provenance attached to records through ingestion and transformation. Establish review and integrity gates before data reaches training or retrieval pipelines.
