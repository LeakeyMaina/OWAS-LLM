# LLM07: Misinformation

## Scenario

The model returns a fluent refund answer with a citation ID, but its deadline does not match the authoritative policy.

## Walk through the code

- `vulnerable.py` defines the structured model draft and displays it without checking.
- `secure.py` verifies the source ID and compares the factual field against the local policy record.
- `demo.py` shows the incorrect answer and the source-based correction.

## Security lesson

A citation-shaped string is not evidence. Verify consequential factual claims against authoritative data, and abstain when a claim cannot be checked.
