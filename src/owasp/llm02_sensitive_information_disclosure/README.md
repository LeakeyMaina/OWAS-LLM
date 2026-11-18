# LLM02: Sensitive Information Disclosure

## Scenario

A customer support app needs to answer a plan question. The unsafe implementation sends every customer row to the model and expects it to pick the right one.

## Walk through the code

- `vulnerable.py` creates synthetic SQLite data and returns every row.
- `secure.py` checks the authenticated identity, uses a parameterized query, and returns only the plan field needed for the task.
- `demo.py` shows the overbroad context and a blocked cross-customer request.

## Security lesson

Authorization and data minimization happen before data enters a prompt. A model is not an access-control layer.
