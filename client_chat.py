# ollama_server.py
import asyncio
import os
from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient
from langchain_ollama import ChatOllama

# async def main():
#     """Run the example using a configuration file."""
#     load_dotenv()
#     # client = MCPClient.from_config_file(os.path.join(os.path.dirname(__file__), "filesystem_mcp.json"))
#     client = MCPClient.from_config_file(os.path.join(os.path.dirname(__file__), "multi_mcp.json"))
#     llm = ChatOllama(
#     model="llama3.1",
#     temperature=0,
#     )
#     agent = MCPAgent(llm=llm, client=client, max_steps=30)
#     print(client)
#     result = await agent.run(
#         "Tell me about study OSD-488.",
#         # "Compare study OSD-1 and OSD-488.",
#         max_steps=30,
#     )
#     print(f"\nResult: {result}")

async def main():
    load_dotenv()
    client = MCPClient.from_config_file(os.path.join(os.path.dirname(__file__), "multi_mcp.json"))
    llm = ChatOllama(model="llama3.1", temperature=0)
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    print("🧠 MCP Agent is ready.")
    print("💬 Type your question (or type 'exit' to quit)\n")

    while True:
        user_input = input("👤 You: ")
        if user_input.strip().lower() in {"exit", "quit"}:
            print("👋 Exiting. See you next time!")
            break

        try:
            result = await agent.run(user_input, max_steps=30)
            print(f"\n🤖 Result:\n{result}\n")
        except Exception as e:
            print(f"⚠️ Error: {e}\n")


if __name__ == "__main__":
    asyncio.run(main())