from typing import Literal, TypedDict


class GraphState(TypedDict):
    """Shared state passed between every node in the graph.

    LangGraph nodes don't share memory directly — each node reads this
    dict, returns the fields it changed, and LangGraph merges that back
    into the state before handing it to the next node.
    """

    process_description: str
    research_findings: str
    analysis: str
    proposal_draft: str
    approval_status: Literal["pending", "approved", "rejected"]
    revision_notes: str
    # Capped at 3 in the routing logic to prevent an infinite
    # Designer <-> Human Review loop if the human keeps rejecting.
    revision_count: int
