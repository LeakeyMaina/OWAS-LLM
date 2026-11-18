"""Unsafe artifact loader that trusts metadata claimed by a download."""

from __future__ import annotations

import json


def load_artifact(artifact: bytes) -> dict[str, object]:
    """Parse model metadata without verifying its source or integrity."""
    return json.loads(artifact)


if __name__ == "__main__":
    unverified_download = (
        b'{"model":"demo-classifier","version":"1.0","loader":"unknown"}'
    )
    print(load_artifact(unverified_download))
