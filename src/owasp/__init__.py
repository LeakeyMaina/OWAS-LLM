"""Entry point for the OWASP LLM security demo collection."""

from __future__ import annotations

import argparse
import runpy
import sys
from collections.abc import Sequence

ISSUES = (
    "llm01_prompt_injection",
    "llm02_sensitive_information_disclosure",
    "llm03_excessive_agency",
    "llm04_supply_chain",
    "llm05_data_model_poisoning",
    "llm06_unbounded_consumption",
    "llm07_misinformation",
    "llm08_hidden_context_exposure",
    "llm09_vector_embedding_weaknesses",
    "llm10_improper_output_handling",
)


def main(argv: Sequence[str] | None = None) -> None:
    """List or run one issue demo by its package name."""
    parser = argparse.ArgumentParser(description="Run an OWASP LLM security demo.")
    parser.add_argument("issue", nargs="?", choices=ISSUES, help="demo package to run")
    arguments, demo_arguments = parser.parse_known_args(argv)

    if arguments.issue is None:
        print("Available demos:")
        for issue in ISSUES:
            print(f"  {issue}")
        print("\nRun one with: owasp <demo-package>")
        return

    module_name = f"owasp.{arguments.issue}.demo"
    previous_argv = sys.argv
    sys.argv = [module_name, *demo_arguments]
    try:
        runpy.run_module(module_name, run_name="__main__")
    finally:
        sys.argv = previous_argv
