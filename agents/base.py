import requests
from tinydb import TinyDB, Query

db = TinyDB("memory/memory_store.json")
Topic = Query()


def call_llm(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt, "stream": False}
    )
    return response.json()["response"].strip()

def log_agent_response(topic: str, agent: str, content: str):
    if db.contains(Topic.name == topic):
        db.update(lambda t: t["log"].append({"agent": agent, "content": content}), Topic.name == topic)
    else:
        db.insert({"name": topic, "log": [{"agent": agent, "content": content}]})

def get_topic_log(topic: str):
    result = db.search(Topic.name == topic)
    return result[0]["log"] if result else []
