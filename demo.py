import asyncio
import os
from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient
from langchain_ollama import ChatOllama

async def main():
    """Run the example using a configuration file."""
    load_dotenv()

    # Get the prompt from the user
    prompt = input("Enter your prompt: ")

    # Create the MCPClient
    client = MCPClient.from_config_file(os.path.join(os.path.dirname(__file__), "all_mcp.json"))

    # Create the LLM
    llm = ChatOllama(
        model="llama3.1",
        temperature=0,
    )

    # Create the agent
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        prompt,
        max_steps=30,
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    while True:
        asyncio.run(main())
        print("\nPress Ctrl+C to exit or run another prompt.\n")