"""Verify downloaded bytes against a separately trusted release digest."""

from __future__ import annotations

import hashlib
import hmac
import json


def load_verified_artifact(artifact: bytes, approved_sha256: str) -> dict[str, object]:
    """Reject an artifact whose bytes differ from the pinned release digest."""
    actual_sha256 = hashlib.sha256(artifact).hexdigest()
    if not hmac.compare_digest(actual_sha256, approved_sha256):
        raise ValueError("Artifact digest does not match the trusted release manifest.")
    return json.loads(artifact)


if __name__ == "__main__":
    approved_release = b'{"model":"demo-classifier","version":"1.0"}'
    approved_digest = hashlib.sha256(approved_release).hexdigest()
    print(load_verified_artifact(approved_release, approved_digest))
