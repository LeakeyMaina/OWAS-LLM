"""Unsafe design that places a credential directly in model-visible context."""

SYSTEM_PROMPT = """You are a support assistant.
Internal API key: demo-key-not-a-real-credential
"""


def build_model_context() -> str:
    """Return instructions that contain a fake but model-visible credential."""
    return SYSTEM_PROMPT


if __name__ == "__main__":
    print(build_model_context())
