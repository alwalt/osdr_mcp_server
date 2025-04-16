import asyncio
import aiohttp
import logging

from mcp.server import Server, InitializationOptions, NotificationOptions
from mcp.server.stdio import stdio_server
from mcp import types

# Optional logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

server = Server("osdr-mcp-server")

# Define your tool(s)
@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="osdr_fetch_metadata",
            description="Fetch dataset metadata from the NASA OSDR API.",
            inputSchema={
                "type": "object",
                "properties": {
                    "dataset_id": {
                        "type": "string",
                        "description": "Accession ID (e.g., 'OSD-488')"
                    }
                },
                "required": ["dataset_id"]
            },
            annotations={
                "title": "Fetch OSDR Dataset Metadata",
                "readOnlyHint": True,
                "openWorldHint": True
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "osdr_fetch_metadata":
        dataset_id = arguments["dataset_id"]
        url = f"https://visualization.osdr.nasa.gov/biodata/api/v2/dataset/{dataset_id}/"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    data = await resp.json()
            return [
                types.TextContent(
                    type="text",
                    text=f"📦 Metadata for {dataset_id}:\n\n{data}"
                )
            ]
        except Exception as e:
            return [
                types.TextContent(
                    type="text",
                    text=f"❌ Error fetching metadata: {str(e)}"
                )
            ]

    return [types.TextContent(type="text", text=f"❌ Unknown tool: {name}")]

# Entry point
def main():
    async def _run():
        logger.info("🚀 Starting native MCP server via stdio...")
        async with stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="osdr-mcp",
                    server_version="0.1.0",
                    capabilities=server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    ),
                )
            )

    asyncio.run(_run())

if __name__ == "__main__":
    main()
