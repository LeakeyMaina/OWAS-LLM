# LLM08: Hidden Context Exposure

## Scenario

An application puts an API credential into the system prompt, assuming that hidden instructions are secret.

## Walk through the code

- `vulnerable.py` places a fake credential in model-visible instructions.
- `secure.py` keeps the credential in server-side environment configuration and returns only non-secret task instructions to the model.
- `demo.py` prints the unsafe context and confirms whether a backend credential is configured without printing its value.

## Security lesson

Anything sent to the model may be repeated, logged, or exposed through a tool. Store credentials in a secret manager and give them only to the backend component that needs them.
