"""Safer fixture path: expose only the read-only capability needed for the task."""

from __future__ import annotations

import json

from owasp.llm01_prompt_injection.scenario import MODEL_TOOL_CALL
from owasp.llm01_prompt_injection.tools import lookup_public_return_policy_data

READ_ONLY_TOOLS = {"lookup_public_return_policy": lookup_public_return_policy_data}


def run() -> str:
    """Reject unknown tool names before dispatching any tool call."""
    call = json.loads(MODEL_TOOL_CALL)
    tool_name = call.get("name")
    if tool_name not in READ_ONLY_TOOLS:
        return f"Blocked: tool {tool_name!r} is not available to this assistant."
    return READ_ONLY_TOOLS[tool_name]()


if __name__ == "__main__":
    print(run())
