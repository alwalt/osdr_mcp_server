# 🧠 OSDR MCP Server + Agents

This repo demonstrates how to integrate MCP agents with custom tools for interacting with NASA’s Open Science Data Repository (OSDR). It includes working examples of agent workflows that fetch, analyze, and summarize biological data using the Model Context Protocol (MCP).

## 📦 What’s Inside

### `osdr_mcp/`
Custom MCP server exposing tools for interacting with OSDR data:
- `osdr_fetch_metadata`: Fetches metadata for a given OSDR dataset
- `osdr_find_by_organism`: Filters studies by organism
- Additional tools (e.g. RNA analysis) live in `osdr_viz_tools`

### `first_example/`
A simple agent that uses two official MCP servers:
- `mcp-server-fetch` (headless browser)
- `mcp-server-filesystem`

This agent gathers information and generates a tweet-sized summary.

### `second_example/`
Similar to `first_example` but connects to a **custom** MCP server defined in `osdr_mcp/main_simple.py`. Demonstrates how to plug in domain-specific tools like OSDR metadata fetchers.

### `third_example/`
A full multi-agent workflow:
1. **Fetch Agent** – Grabs OSD study metadata
2. **Quant Analysis Agent** – Downloads RNA count data and creates a bar plot
3. **Summary Writer Agent** – Generates a markdown report summarizing the analysis

Uses custom MCP servers:  
- `osdr_data_fetch`  
- `osdr_viz_tools`

## ⚙️ Configuration

The `cp_agent.config.yaml` file controls:
- LLM backend (e.g. Ollama, OpenAI)
- MCP server connections
- Tool availability
- System prompts / metadata

## 🚀 Getting Started

1. Clone this repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run an example:
   ```bash
   python first_example/main.py
   ```

Or launch the MCP server directly:
```bash
python osdr_mcp/main_simple.py
```

## 🧩 Integration Notes

This architecture is built for flexibility. You can toggle between document Q&A, RAG search, or custom analysis tools. A mode switch or UI toggle is ideal for user-facing integration. Support for Milvus-based RAG via MCP is on the roadmap.

## 📚 Resources

- [Model Context Protocol](https://modelcontext.org/)
- [NASA OSDR API](https://visualization.osdr.nasa.gov/biodata/api/v2/dataset/)
