"""Smoke tests: the graph builds and the state schema is what we expect.

No real API calls happen here — compiling a graph never invokes the LLM,
so a fake API key is enough to satisfy ChatAnthropic's constructor.
"""


def test_graph_compiles(monkeypatch):
    # graph.py constructs ChatAnthropic at import time, which requires
    # ANTHROPIC_API_KEY to be set — fake it before the import happens.
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key-not-real")
    from src.graph import build_graph

    graph = build_graph()
    assert graph is not None


def test_graph_state_has_expected_fields():
    from src.state import GraphState

    expected = {
        "process_description",
        "research_findings",
        "analysis",
        "proposal_draft",
        "approval_status",
        "revision_notes",
        "revision_count",
    }
    assert set(GraphState.__annotations__) == expected
