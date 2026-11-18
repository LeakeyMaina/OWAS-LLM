"""Small, local-only tools used to make the prompt-injection risk concrete."""

from __future__ import annotations

from dataclasses import dataclass, field

from langchain.tools import tool

PRIVATE_ORDER_NOTE = "Demo order 4821: replacement shipment approved"


@dataclass(slots=True)
class DemoOutbox:
    """In-memory sink that stands in for an email provider."""

    messages: list[dict[str, str]] = field(default_factory=list)

    def send(self, recipient: str, body: str) -> str:
        """Record a message locally; this demo never sends real email."""
        self.messages.append({"to": recipient, "body": body})
        return f"Demo email recorded for {recipient}."


DEMO_OUTBOX = DemoOutbox()


def lookup_public_return_policy_data() -> str:
    """Return the policy through the application's local data service."""
    return "Returns are accepted within 30 days."


@tool
def lookup_public_return_policy() -> str:
    """Return the public return policy without reading customer data."""
    return lookup_public_return_policy_data()


@tool
def email_private_order_note(recipient: str) -> str:
    """Email the signed-in customer's private order note to a recipient.

    Args:
        recipient: Email address that receives the note.
    """
    # This intentionally overpowered tool fetches private data on the server side.
    return DEMO_OUTBOX.send(recipient, PRIVATE_ORDER_NOTE)


def record_demo_email(recipient: str, body: str) -> str:
    """Call the same local side-effect sink from the offline fixture demo."""
    return DEMO_OUTBOX.send(recipient, body)
