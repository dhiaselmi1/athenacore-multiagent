from .base import call_llm, log_agent_response, get_topic_log
def run(topic: str):
    memory = "\n".join([m["content"] for m in get_topic_log(topic)])
    prompt = f"Extract key insights or takeaways from this content:\n\n{memory}"
    insight = call_llm(prompt)
    log_agent_response(topic, "Insight Agent", insight)
    return insight