# ollama_server.py
import asyncio
import os
from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient
from langchain_ollama import ChatOllama

async def main():
    """Run the example using a configuration file."""
    load_dotenv()
    # client = MCPClient.from_config_file(os.path.join(os.path.dirname(__file__), "filesystem_mcp.json"))
    client = MCPClient.from_config_file(os.path.join(os.path.dirname(__file__), "osdr_server.json"))
    llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    )
    agent = MCPAgent(llm=llm, client=client, max_steps=3)
    print(client)
    result = await agent.run(
        "Fetch OSD-488 dataset from the OSDR API",
        # "Find the best restaurant in San Francisco USING GOOGLE SEARCH",
        max_steps=3,
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())