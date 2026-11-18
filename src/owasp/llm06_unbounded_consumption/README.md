# LLM06: Unbounded Consumption

## Scenario

An inference endpoint accepts arbitrarily large prompts and has no generation cap or per-user usage budget.

## Walk through the code

- `vulnerable.py` leaves input and output limits unset.
- `secure.py` estimates input size, caps output, and checks that the request fits the user's remaining budget before it is sent.
- `demo.py` runs a representative short prompt through both paths.

## Security lesson

Use provider tokenizers and usage reports in production. Reserve budget atomically, enforce rate and concurrency limits, and cap every source of model and tool work.
