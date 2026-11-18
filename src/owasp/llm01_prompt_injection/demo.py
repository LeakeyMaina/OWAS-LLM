"""Run the deterministic prompt-injection demo, or opt into a live model run."""

from __future__ import annotations

import argparse

from owasp.llm01_prompt_injection import secure, vulnerable
from owasp.llm01_prompt_injection.scenario import ATTACKER_CONTROLLED_ARTICLE


def main() -> None:
    """Print vulnerable and safer outcomes from a fixed model-call fixture."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--live",
        action="store_true",
        help="call LangChain and LangGraph (requires OPENAI_API_KEY)",
    )
    arguments = parser.parse_args()

    if arguments.live:
        from owasp.llm01_prompt_injection.live_demo import main as live_main

        live_main()
        return

    print("Retrieved untrusted article:\n" + ATTACKER_CONTROLLED_ARTICLE)
    print("\nVulnerable app:", vulnerable.run())
    print("Safer app:     ", secure.run())


if __name__ == "__main__":
    main()
