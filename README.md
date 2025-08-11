# 🧠 AthenaCore: Multi-Agent AI Collaboration with Persistent Memory

AthenaCore is a **collaborative multi-agent AI system** where multiple specialized agents work together to research, summarize, challenge ideas, and extract insights — all sharing a **persistent topic memory**. This setup allows for **continuity across sessions**, evolving knowledge bases, and dynamic agent orchestration via a user-friendly **Streamlit frontend**.

---

## 🚀 Features

-   **Multiple AI Agents with Specialties**
    -   **Research Agent** – Finds factual answers & gathers context.
    -   **Summarizer Agent** – Condenses raw text into concise bullet points.
    -   **Devil’s Advocate Agent** – Challenges assumptions and raises counterpoints.
    -   **Insight Agent** – Extracts actionable takeaways from conversation history.
-   **Shared Persistent Memory**
    -   All agents contribute to a **topic-specific memory log** stored in TinyDB.
    -   Memory grows as discussions progress, improving context awareness.
-   **Flexible Execution**
    -   Run any agent independently.
    -   Orchestrate a **team run**: `Research → Summarizer → Devil → Insight`.
-   **Streamlit Interface**
    -   Create/select topics.
    -   Run agents or team pipelines.
    -   View and browse historical logs.
-   **Local LLM Support**
    -   Works with **LLaMA 2** or **Mistral** models via [Ollama](https://ollama.ai/).

---

## 📂 Project Structure

```
athenacore-multiagent/
├── agents/
│   ├── base.py
│   ├── research_agent.py
│   ├── summarizer_agent.py
│   ├── devil_agent.py
│   └── insight_agent.py
├── orchestrator.py
├── memory/
│   └── memory_store.json
├── frontend.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Install Ollama

Follow the official instructions at: [https://ollama.ai/download](https://ollama.ai/download)

### 2️⃣ Pull a Supported Model

Choose one of the following models to pull:

```bash
ollama pull llama2
```

or

```bash
ollama pull mistral
```

### 3️⃣ Clone the Repository

```bash
git clone [https://github.com/](https://github.com/)<your-username>/athenacore-multiagent.git
cd athenacore-multiagent
```

### 4️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Start the Ollama Server

Open a new terminal and run the model. This will start the server required by AthenaCore.

```bash
ollama run llama2
```

### 6️⃣ Launch the AthenaCore UI

In your project directory, launch the Streamlit application.

```bash
streamlit run frontend.py
```

---

## 🖥️ Usage Guide

1.  Start the app: `streamlit run frontend.py`
2.  In the web interface, create a new topic or select a pre-existing one from the sidebar.
3.  Choose an agent to run from the dropdown menu:
    -   **Research** – Provide a specific query for the agent to investigate.
    -   **Summarizer** – Generates a concise summary of the entire conversation history for the topic.
    -   **Devil** – Raises counterpoints and challenges based on the current discussion.
    -   **Insight** – Extracts key, actionable takeaways from the memory log.
4.  Click the "Run Agent" button to execute a single agent, or "Run Team" to run all agents in a coordinated sequence.
5.  View the "Memory Log" section to track how the topic's knowledge base evolves over time.

---

## 📜 Example Workflow

**Topic:** "AI and Global Regulation"

1.  **Research Agent**: User provides the query "What are the latest developments in AI regulation in the EU and US?". The agent finds recent articles and legal frameworks.
2.  **Summarizer Agent**: The agent condenses the raw research findings into key bullet points, which are added to the memory.
3.  **Devil’s Advocate Agent**: The agent reviews the summary and poses questions like, "Could over-regulation stifle innovation? What are the arguments against the EU's AI Act?".
4.  **Insight Agent**: After the discussion, this agent analyzes the memory to identify strategic insights, such as "Conclusion: A balanced approach is needed, where regulation protects consumers without hindering technological progress. Key areas of contention are data privacy and algorithmic transparency."

---

## 🧩 Tech Stack

-   **Backend Logic**: Python
-   **Database**: TinyDB (for simple JSON-based persistent storage)
-   **Frontend**: Streamlit
-   **AI Models**: LLaMA 2 / Mistral via Ollama
-   **Orchestration**: Custom multi-agent pipeline logic

---

## 📦 requirements.txt

```text
streamlit
tinydb
requests
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the project repository.
2.  Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.
