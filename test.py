import asyncio
import aiohttp

class OSDRConnector:
    BASE_URL = "https://visualization.osdr.nasa.gov/biodata/api"

    def __init__(self):
        pass

    async def fetch_dataset_metadata(self, dataset_id: str) -> dict:
        url = f"{self.BASE_URL}/v2/dataset/{dataset_id}/"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

async def main():
    connector = OSDRConnector()

    print("\n🔍 Testing fetch_dataset_metadata('OSD-48')...")
    metadata = await connector.fetch_dataset_metadata("OSD-48")
    print(metadata)

if __name__ == "__main__":
    asyncio.run(main())