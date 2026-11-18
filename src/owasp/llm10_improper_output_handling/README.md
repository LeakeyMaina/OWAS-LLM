# LLM10: Improper Output Handling

## Scenario

A model repeats HTML from a support ticket, and the application inserts it directly into a dashboard page.

## Walk through the code

- `vulnerable.py` interpolates model text into an HTML fragment as active markup.
- `secure.py` escapes the text for an HTML text-node context.
- `demo.py` prints both renderings.

## Security lesson

Treat model output like untrusted user input at every downstream sink. Use context-specific encoding, parameterized database operations, safe subprocess APIs, and framework autoescaping as appropriate.
