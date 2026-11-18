# LLM03: Excessive Agency

## Scenario

An account-support agent receives a request to delete an account. A model-selected tool call is only a proposal; the application must decide whether the user is authorized and whether a person must approve the action.

## Walk through the code

- `tools.py` defines actual LangChain tools with `@tool`. The deletion tool mutates only an in-memory demo store. The read-only graph does not expose it.
- `vulnerable.py` shows the unsafe pattern of executing the requested action immediately.
- `secure.py` gives the assistant only a read tool and checks the requested customer against authenticated identity. A separate deletion flow requires both an identity match and explicit confirmation supplied by the application.
- `demo.py` runs both examples against separate in-memory stores.

## Security lesson

Use the smallest capability set, enforce authorization at the tool boundary, and require separate human approval for high-impact changes. A model-generated argument is not user consent.
