# Intelligent Process Automation Advisor

[![CI](https://github.com/Vlue001/automation-advisor-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/Vlue001/automation-advisor-agent/actions/workflows/ci.yml)

> Work in progress — a LangGraph multi-agent system that takes a plain-language business process description and drafts an automation proposal, with a human-in-the-loop approval/revision loop.

This is my second AI agent portfolio project (after a completed [CrewAI research agent](https://github.com/Vlue001/crewai-research-agent)) and my first time using LangGraph. Inspired by the kind of RPA + ML/AI workflow automation work done by teams like Bosch Service Solutions' Software & AI Automation group — built as a genuine learning project, not a copied case study.

## How it works (planned)

```
Research → Analyst → Designer → Human Review → (approved: finalize | rejected: back to Designer)
```

4 nodes in a LangGraph `StateGraph`, with a conditional loop back to the Designer node when a human reviewer requests revisions (capped at 3 revision cycles).

## Status

🚧 Just getting started — repo and folder skeleton only so far. See commit history for progress.

## Tech stack

`langgraph`, `langchain-anthropic`, `python-dotenv`, `pytest`, `ruff`

## Project structure

```
automation-advisor-agent/
├── src/
│   ├── nodes/
│   │   ├── research_node.py
│   │   ├── analyst_node.py
│   │   ├── designer_node.py
│   │   └── human_review_node.py
│   ├── state.py
│   └── graph.py
├── tests/
├── main.py
├── requirements.txt
└── .env.example
```

## License

MIT
