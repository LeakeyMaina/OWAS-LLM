"""Shared LangGraph builder for small LangChain tool-calling examples."""

from __future__ import annotations

import os
from collections.abc import Sequence

from langchain_core.messages import AnyMessage, SystemMessage
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition


def build_tool_graph(
    *,
    tools: Sequence[BaseTool],
    system_prompt: str,
    model_name: str | None = None,
):
    """Build a model → tool → model graph with a fixed, explicit tool set."""
    if not tools:
        raise ValueError("At least one tool is required to build this graph.")

    selected_model = model_name or os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
    model = ChatOpenAI(model=selected_model, temperature=0).bind_tools(tools)

    def call_model(state: MessagesState) -> dict[str, list[AnyMessage]]:
        messages = [SystemMessage(content=system_prompt), *state["messages"]]
        return {"messages": [model.invoke(messages)]}

    graph = StateGraph(MessagesState)
    graph.add_node("assistant", call_model)
    graph.add_node("tools", ToolNode(tools))
    graph.add_edge(START, "assistant")
    graph.add_conditional_edges(
        "assistant",
        tools_condition,
        {"tools": "tools", END: END},
    )
    graph.add_edge("tools", "assistant")
    return graph.compile()
