"""Hello-world graph: confirms LangGraph + Claude wiring works end to end.

Two nodes, no branching yet — just proves the plumbing (state passing,
an LLM call via langchain-anthropic, graph compile/invoke) before the
real Research/Analyst/Designer/Human-Review nodes get built in Week 2.
"""

import sys

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langgraph.graph import END, START, StateGraph

from src.state import GraphState

# Must run before ChatAnthropic() is constructed below, since it reads
# ANTHROPIC_API_KEY from the environment at construction time.
load_dotenv()

llm = ChatAnthropic(model="claude-sonnet-4-5")


def greet_node(state: GraphState) -> dict:
    return {"research_findings": f"Hello world for: {state['process_description']}"}


def respond_node(state: GraphState) -> dict:
    response = llm.invoke(state["research_findings"])
    return {"analysis": response.content}


def build_graph():
    builder = StateGraph(GraphState)
    builder.add_node("greet", greet_node)
    builder.add_node("respond", respond_node)
    builder.add_edge(START, "greet")
    builder.add_edge("greet", "respond")
    builder.add_edge("respond", END)
    return builder.compile()


if __name__ == "__main__":
    # Windows console defaults to cp1252, which chokes on characters
    # like the arrow above — force UTF-8 so LLM output prints safely.
    sys.stdout.reconfigure(encoding="utf-8")
    graph = build_graph()
    result = graph.invoke({"process_description": "testing the graph wiring"})
    print(result["analysis"])
