# Calculator MCP Agent

A LangChain agent that connects to a custom [MCP](https://modelcontextprotocol.io/)
(Model Context Protocol) server which exposes a simple **calculator** tool. The
agent can evaluate mathematical expressions by calling the calculator tool over
MCP.

This is a **LangChain course learning project** — it was built to explore how
LangChain agents integrate with MCP servers and local LLMs.

## How it works

- `mcqcalc.py` — a FastMCP server that exposes a `calculator` tool (and a prompt
  template) over streamable HTTP.
- `mcp_calc.ipynb` — a notebook that starts a LangChain agent, connects to the
  MCP server, and uses a locally hosted Ollama model to answer math questions.

## Running it

Running this project takes **two steps, in two separate terminals**.

1. **Start the MCP server** in one terminal:

   ```bash
   python mcqcalc.py
   ```

   This launches the calculator MCP server (listening on port 8000).

2. **Run the notebook** in another terminal (or your editor):

   Open and run `mcp_calc.ipynb`. It connects to the running MCP server and
   drives the agent.

## ⚠️ Ollama configuration

The notebook's `base_url` for Ollama points to a **private local network
address** specific to the original author's setup. Before running the notebook,
**replace that `base_url` with your own Ollama instance URL** (for example,
`http://localhost:11434` if you run Ollama locally).

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file for any required environment variables (it is git-ignored).
