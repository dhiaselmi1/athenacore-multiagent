# orchestrator.py
from agents import research_agent, summarizer_agent, devil_agent, insight_agent

def run_agent(agent: str, topic: str, query: str = "") -> str:
    key = agent.strip().lower()
    if key == "research":
        return research_agent.run(topic, query)
    if key == "summarizer":
        return summarizer_agent.run(topic)
    if key in ("devil", "devil’s advocate", "devil's advocate"):
        return devil_agent.run(topic)
    if key == "insight":
        return insight_agent.run(topic)
    raise ValueError(f"Unknown agent: {agent}")

def team_run(topic: str, query: str = "") -> dict:
    """Run Research → Summarizer → Devil → Insight and return outputs."""
    outputs = {}
    outputs["Research"]   = research_agent.run(topic, query)
    outputs["Summarizer"] = summarizer_agent.run(topic)
    outputs["Devil"]      = devil_agent.run(topic)
    outputs["Insight"]    = insight_agent.run(topic)
    return outputs
