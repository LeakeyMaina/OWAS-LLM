"""Keep credentials in server-side configuration, outside model-visible text."""

from os import environ

SYSTEM_PROMPT = "You are a support assistant. Answer questions about public policies."


def build_model_context() -> str:
    """Return task instructions without credentials or internal secrets."""
    return SYSTEM_PROMPT


def get_backend_credential() -> str | None:
    """Read a credential for trusted backend use only."""
    return environ.get("SUPPORT_API_KEY")


if __name__ == "__main__":
    print(build_model_context())
    print("Backend credential configured:", get_backend_credential() is not None)
