# app.py (your Streamlit UI)
import streamlit as st
from orchestrator import run_agent, team_run
from tinydb import TinyDB, Query
from datetime import datetime
import json

db = TinyDB("memory/memory_store.json")
Topic = Query()

def list_topics():
    return [t.get("name") for t in db.all() if t.get("name")]

def ensure_topic(name: str):
    if name and not db.search(Topic.name == name):
        db.insert({"name": name, "log": []})

st.set_page_config(page_title="AthenaCore", page_icon="🧠", layout="wide")
st.title("🧠 AthenaCore: Multi-Agent Collaboration with Memory")

topics = list_topics()
topic = st.selectbox("Choose a topic", options=(topics + ["➕ New Topic"]) if topics else ["➕ New Topic"])
if topic == "➕ New Topic":
    topic = st.text_input("New topic name", placeholder="e.g., AI in Healthcare")

agent_choice = st.selectbox("Agent", ["Research", "Summarizer", "Devil", "Insight"])
query = st.text_area("Query / context (used by Research)", "")

cols = st.columns([1,1,6])
with cols[0]:
    if st.button("Run Agent", use_container_width=True) and topic:
        ensure_topic(topic)
        with st.spinner("Running agent…"):
            result = run_agent(agent_choice, topic, query)
        st.subheader(f"{agent_choice} Agent Output")
        st.write(result)

with cols[1]:
    if st.button("Run All Agents", use_container_width=True) and topic:
        ensure_topic(topic)
        with st.spinner("Running team pipeline (Research → Summarizer → Devil → Insight)…"):
            outputs = team_run(topic, query)
        st.subheader("Team Output")
        for k in ["Research", "Summarizer", "Devil", "Insight"]:
            with st.expander(k, expanded=(k=="Insight")):
                st.write(outputs.get(k, ""))

st.divider()
st.markdown("### 📜 Shared Topic Log")
doc = db.search(Topic.name == topic)
if doc:
    for entry in doc[0]["log"][::-1]:
        st.markdown(f"**{entry.get('agent','?')}** · _{entry.get('timestamp','')}_")
        st.write(entry.get("content",""))
        st.markdown("---")
else:
    st.info("Aucun log pour ce topic (encore). Lance un agent pour démarrer.")
