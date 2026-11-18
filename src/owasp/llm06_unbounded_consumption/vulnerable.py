"""Unbounded request builder with no size, output, or user budget controls."""

from __future__ import annotations


def build_request(prompt: str) -> dict[str, str | None]:
    """Return a request with unlimited input and generation size."""
    return {"prompt": prompt, "max_output_tokens": None}


if __name__ == "__main__":
    print(build_request("Summarize this support ticket."))
