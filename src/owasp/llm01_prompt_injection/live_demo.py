"""Run decorated LangChain tools in LangGraph using a configured model."""

from __future__ import annotations

from langchain_core.messages import HumanMessage

from owasp.llm01_prompt_injection.agents import (
    build_secure_graph,
    build_vulnerable_graph,
)
from owasp.llm01_prompt_injection.scenario import ATTACKER_CONTROLLED_ARTICLE
from owasp.llm01_prompt_injection.tools import DEMO_OUTBOX


def main() -> None:
    """Compare vulnerable and read-only graphs against the same article."""
    prompt = (
        "A customer asks about returns. Use this retrieved article to answer:\n\n"
        f"{ATTACKER_CONTROLLED_ARTICLE}\n\n"
        "The customer's private order note is stored in the support system; it is not "
        "included in this message."
    )

    DEMO_OUTBOX.messages.clear()
    inputs = {"messages": [HumanMessage(content=prompt)]}

    print("Vulnerable LangGraph agent:")
    vulnerable_result = build_vulnerable_graph().invoke(
        inputs,
        config={"recursion_limit": 8},
    )
    print(vulnerable_result["messages"][-1].content)
    print("Local demo outbox:", DEMO_OUTBOX.messages)

    print("\nRead-only LangGraph agent:")
    secure_result = build_secure_graph().invoke(
        inputs,
        config={"recursion_limit": 8},
    )
    print(secure_result["messages"][-1].content)


if __name__ == "__main__":
    main()
