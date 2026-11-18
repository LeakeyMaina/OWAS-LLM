"""Compare trusting a downloaded model with verifying its pinned digest."""

import hashlib

from owasp.llm04_supply_chain.secure import load_verified_artifact
from owasp.llm04_supply_chain.vulnerable import load_artifact

APPROVED_RELEASE = b'{"model":"support-classifier","version":"1.2.0"}'
TAMPERED_DOWNLOAD = (
    b'{"model":"support-classifier","version":"1.2.0","loader":"unknown"}'
)
APPROVED_DIGEST = hashlib.sha256(APPROVED_RELEASE).hexdigest()


def main() -> None:
    """Print the unverified metadata and show the tampered bytes are rejected."""
    print("Vulnerable loader:", load_artifact(TAMPERED_DOWNLOAD))
    try:
        load_verified_artifact(TAMPERED_DOWNLOAD, APPROVED_DIGEST)
    except ValueError as error:
        print("Verified loader blocked artifact:", error)


if __name__ == "__main__":
    main()
