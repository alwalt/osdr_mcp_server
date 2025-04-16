from mcp.server.fastmcp import FastMCP, Image
import httpx

mcp = FastMCP("OSDR_MCP_Server")

@mcp.tool()
async def fetch_dataset_metadata(dataset_id: str) -> dict:
    """
    Fetch minimal metadata needed for terminal comparison.
    """
    url = f"https://visualization.osdr.nasa.gov/biodata/api/v2/dataset/{dataset_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    metadata = data.get(dataset_id, {}).get("metadata", {})
    return {
        "dataset_id": dataset_id,
        "title": metadata.get("study title", "N/A"),
        "organism": metadata.get("organism", "N/A"),
        "mission": ", ".join(metadata.get("mission", {}).get("name", [])) or "N/A",
        "protocols": metadata.get("study protocol name", []),
        "assay_type": metadata.get("study assay technology type", "N/A"),
        "platform": metadata.get("study assay technology platform", "N/A"),
        "funding": metadata.get("study funding agency", "N/A"),
    }


if __name__ == "__main__":
    mcp.run(transport='stdio')
