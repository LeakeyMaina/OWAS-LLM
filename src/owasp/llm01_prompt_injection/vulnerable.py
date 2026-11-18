"""Unsafe fixture path: retrieved instructions can trigger a data-leaking tool."""

from __future__ import annotations

import json

from owasp.llm01_prompt_injection.scenario import MODEL_TOOL_CALL
from owasp.llm01_prompt_injection.tools import PRIVATE_ORDER_NOTE, record_demo_email


def run() -> str:
    """Execute model-produced arguments with no user authorization check."""
    call = json.loads(MODEL_TOOL_CALL)
    if call["name"] == "email_private_order_note":
        return record_demo_email(
            call["arguments"]["recipient"], PRIVATE_ORDER_NOTE
        )
    return "Unknown tool"


if __name__ == "__main__":
    print(run())
