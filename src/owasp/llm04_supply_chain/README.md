# LLM04: Supply Chain

## Scenario

A service downloads a model artifact. The JSON metadata looks plausible, but the downloaded bytes differ from the reviewed release.

## Walk through the code

- `vulnerable.py` trusts parseable metadata.
- `secure.py` computes SHA-256 and compares it to a digest supplied through a trusted release channel, using a constant-time comparison.
- `demo.py` modifies a synthetic artifact and shows that verification rejects it.

## Security lesson

A digest is useful only when the expected value is obtained through a separately protected, authenticated release process. In production, also verify signatures, provenance, dependencies, and artifact-loading behavior.
