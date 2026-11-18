"""Bound request size and reserve a per-user token budget before generation."""

from __future__ import annotations

MAX_INPUT_TOKENS = 256
MAX_OUTPUT_TOKENS = 128
DAILY_TOKEN_BUDGET = 1_000


def estimate_tokens(text: str) -> int:
    """Return a conservative teaching estimate, not a provider tokenizer result."""
    return max(1, (len(text) + 3) // 4)


def build_bounded_request(prompt: str, used_today: int) -> dict[str, int | str]:
    """Reject oversized requests and reserve input plus maximum output tokens."""
    if used_today < 0:
        raise ValueError("Token usage cannot be negative.")
    input_tokens = estimate_tokens(prompt)
    if input_tokens > MAX_INPUT_TOKENS:
        raise ValueError(f"Input estimate exceeds {MAX_INPUT_TOKENS} tokens.")

    reservation = input_tokens + MAX_OUTPUT_TOKENS
    if used_today + reservation > DAILY_TOKEN_BUDGET:
        raise RuntimeError("Request would exceed this user's daily token budget.")

    return {
        "prompt": prompt,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "reserved_tokens": reservation,
    }


if __name__ == "__main__":
    print(build_bounded_request("Summarize this support ticket.", used_today=100))
