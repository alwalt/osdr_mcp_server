import aiohttp

class OSDRConnector:
    BASE_URL = "https://visualization.osdr.nasa.gov/biodata/api"

    def __init__(self):
        pass  # No auth required for public API

    async def fetch_dataset_metadata(self, dataset_id: str) -> dict:
        url = f"{self.BASE_URL}/v2/dataset/{dataset_id}/"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()