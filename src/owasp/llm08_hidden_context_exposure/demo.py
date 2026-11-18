"""Show why secrets must stay outside the model's input and outputs."""

from owasp.llm08_hidden_context_exposure.secure import (
    build_model_context as secure_context,
)
from owasp.llm08_hidden_context_exposure.secure import get_backend_credential
from owasp.llm08_hidden_context_exposure.vulnerable import (
    build_model_context as vulnerable_context,
)


def main() -> None:
    """Print the fake unsafe prompt and the secret-free safe context."""
    print("Unsafe model context:\n", vulnerable_context())
    print("Safe model context:  ", secure_context())
    print("Backend credential configured:", get_backend_credential() is not None)


if __name__ == "__main__":
    main()
