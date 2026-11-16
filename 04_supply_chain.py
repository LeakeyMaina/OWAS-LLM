"""LLM04: Supply-chain integrity for a downloaded model artifact."""

from hashlib import sha256
import json

# In production, this digest comes from a signed release manifest, not the download.
APPROVED_MODEL_SHA256 = sha256(b'{"model":"support-classifier","version":"1.2.0"}').hexdigest()
DOWNLOADED_MODEL = b'{"model":"support-classifier","version":"1.2.0","post_install":"unknown"}'


def load_without_verification(artifact: bytes) -> dict:
    # Parses metadata and trusts the artifact's claimed identity/version.
    return json.loads(artifact)


def verify_before_load(artifact: bytes, approved_digest: str) -> dict:
    actual_digest = sha256(artifact).hexdigest()
    if actual_digest != approved_digest:
        raise ValueError("Downloaded model does not match the approved release")
    return json.loads(artifact)


if __name__ == "__main__":
    print("Vulnerable loader trusted:", load_without_verification(DOWNLOADED_MODEL))
    try:
        print("Verified loader:", verify_before_load(DOWNLOADED_MODEL, APPROVED_MODEL_SHA256))
    except ValueError as error:
        print("Verified loader blocked artifact:", error)
