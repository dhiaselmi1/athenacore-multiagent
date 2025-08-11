from .base import call_llm, log_agent_response, get_topic_log

def run(topic: str):
    memory = "\n".join([m["content"] for m in get_topic_log(topic)])
    prompt = f"Summarize the following content in 3 bullet points:\n\n{memory}"
    summary = call_llm(prompt)
    log_agent_response(topic, "Summarizer Agent", summary)
    return summary