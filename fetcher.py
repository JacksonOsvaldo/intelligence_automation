import httpx
import pandas as pd

def fetch_products():
    url = "https://fakestoreapi.com/products"
    with httpx.Client(verify=False) as client:
        response = client.get(url)
        response.raise_for_status()
        data = response.json()
    return pd.DataFrame(data)