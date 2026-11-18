# LLM01: Prompt Injection

## Scenario

A support assistant retrieves a return-policy article. An attacker has added a sentence asking the assistant to email a private order note. Retrieved text is untrusted input even when it looks like ordinary documentation.

## Walk through the code

1. `tools.py` defines two schema-backed LangChain tools using `@tool`. The email tool reads a synthetic private note from a server-side fixture and writes only to an in-memory demo outbox; it cannot send real email.
2. `vulnerable.py` models an unsafe tool call. It dispatches the model's requested email action without checking whether the customer authorized it.
3. `secure.py` represents a read-only assistant. Its tool allowlist contains only the public policy lookup, so an email request is rejected before dispatch.
4. `agents.py` builds LangGraph workflows around the decorated tools. The vulnerable graph gets the private-note email capability; the secure graph does not.

## Run it

Offline fixture, no API key or network call:

```bash
owasp llm01_prompt_injection
```

Optional live model call through LangChain and LangGraph (requires `OPENAI_API_KEY`):

```bash
owasp llm01_prompt_injection --live
```

## Security lesson

Prompt wording can guide a model but cannot enforce authorization. Give each graph only task-required tools, treat retrieved and tool-produced content as untrusted, validate arguments, and authorize consequential actions in application code.
