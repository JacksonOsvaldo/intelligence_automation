def analyze_sales(df_sales):
    total_revenue = df_sales['total'].sum()
    avg_revenue = df_sales.groupby('date')['total'].sum().mean()
    top_product = df_sales.groupby('title')['total'].sum().idxmax()
    top_day = df_sales.groupby('date')['total'].sum().idxmax()

    return {
        "total_revenue": total_revenue,
        "avg_daily_revenue": avg_revenue,
        "top_product": top_product,
        "top_day": top_day
    }
