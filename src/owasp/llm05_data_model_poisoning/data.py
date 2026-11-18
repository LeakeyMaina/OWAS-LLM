"""Synthetic feedback export used by the poisoning example."""

from csv import DictReader
from io import StringIO

TRAINING_EXPORT = """question,answer,source,reviewed,integrity_verified
How long are refunds available?,30 days,approved_policy,true,true
How do I reset my password?,Use the password reset page,approved_policy,true,true
How long are refunds available?,365 days,public_feedback,false,false
"""


def load_feedback_rows() -> list[dict[str, str]]:
    """Parse the CSV fixture into records while retaining provenance fields."""
    return list(DictReader(StringIO(TRAINING_EXPORT)))
