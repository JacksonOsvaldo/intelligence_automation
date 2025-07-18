import pandas as pd
import random
from datetime import datetime, timedelta

def simulate_sales(df_products: pd.DataFrame, days: int = 7) -> pd.DataFrame:
    sales_data = []
    for i in range(days):
        date = datetime.now() - timedelta(days=i)
        for _, product in df_products.iterrows():
            quantity = random.randint(0, 5)
            if quantity > 0:
                sales_data.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "product_id": product['id'],
                    "title": product['title'],
                    "price": product['price'],
                    "quantity": quantity,
                    "total": round(product['price'] * quantity, 2)
                })
    return pd.DataFrame(sales_data)
