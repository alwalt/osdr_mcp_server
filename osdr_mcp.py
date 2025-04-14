# from mcp.server.fastmcp import FastMCP, Image
import httpx
# from viz_utils import fetch_osdr_data 
import pandas as pd
# ; import matplotlib
# ; matplotlib.use('Agg')
# ; import matplotlib.pyplot as plt
# ; import seaborn as sns
# ; from sklearn.decomposition import PCA
import requests
from io import StringIO
# ; from csv import Sniffer
# ; from PIL import Image as PILImage  # Not strictly needed unless you do validation
# ; from io import BytesIO
from csv import Sniffer

def detect_separator(text):
    dialect = Sniffer().sniff(text.splitlines()[0])
    return dialect.delimiter

def fetch_osdr_data(url):
    print(f"Fetching data from {url}")
    response = requests.get(url)
    response.raise_for_status()

    if "text/html" in response.headers.get("Content-Type", ""):
        raise ValueError("Received HTML instead of data.")

    preview = response.text[:1000]
    sep = detect_separator(preview)
    df = pd.read_csv(StringIO(response.text), sep=sep)
    
    if df.empty or len(df.columns) == 1:
        print("❌ Malformed data:")
        print(df.head())
        raise ValueError("Data likely has wrong separator or bad formatting.")
    
    return df

async def fetch_study_info(dataset_id: str) -> dict:
    """
    Fetch study description and protocol description for a given dataset.
    """
    url = f"https://visualization.osdr.nasa.gov/biodata/api/v2/dataset/{dataset_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    metadata = data.get(dataset_id, {}).get("metadata", {})
    return {
        "dataset_id": dataset_id,
        "study_description": metadata.get("study description", ""),
        "protocol_descriptions": metadata.get("study protocol description", []),
    }

if __name__ == "__main__":
    # Example usage
    dataset_id = "OSD-488"  # Replace with actual dataset ID
    study_info = fetch_study_info(dataset_id)
    print(study_info)

    # Example URL for fetching data
    url = "https://visualization.osdr.nasa.gov/biodata/api/v2/dataset/OSD-488"  # Replace with actual URL
    df = fetch_osdr_data(url)
    print(df.head())