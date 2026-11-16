"""LLM06: Bound an API request by tokens, output, and per-user budget."""

MAX_INPUT_TOKENS = 80
MAX_OUTPUT_TOKENS = 120
DAILY_TOKEN_BUDGET = 500


def estimate_tokens(text: str) -> int:
    # Conservative teaching approximation; production should use provider usage/tokenizer.
    return max(1, (len(text) + 3) // 4)


def vulnerable_request(prompt: str) -> dict:
    # An API wrapper with no input cap, max output, or account budget.
    return {"prompt": prompt, "max_output_tokens": None}


def bounded_request(prompt: str, used_today: int) -> dict:
    input_tokens = estimate_tokens(prompt)
    if input_tokens > MAX_INPUT_TOKENS:
        raise ValueError(f"Input is {input_tokens} tokens; limit is {MAX_INPUT_TOKENS}")
    reserved = input_tokens + MAX_OUTPUT_TOKENS
    if used_today + reserved > DAILY_TOKEN_BUDGET:
        raise RuntimeError("Request would exceed this user's daily token budget")
    return {
        "prompt": prompt,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "reserved_tokens": reserved,
    }


if __name__ == "__main__":
    request = "Summarize this support ticket in one sentence."
    print("Vulnerable API request:", vulnerable_request(request))
    print("Bounded API request:   ", bounded_request(request, used_today=100))
