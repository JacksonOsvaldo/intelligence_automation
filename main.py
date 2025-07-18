from intelligence_automation.fetcher import fetch_products
from intelligence_automation.simulator import simulate_sales
from intelligence_automation.analyzer import analyze_sales
from intelligence_automation.summarizer import summarize_insights

def run():
    print("Buscando produtos...")
    products_df = fetch_products()

    print("Simulando vendas...")
    sales_df = simulate_sales(products_df)

    print("Analisando vendas...")
    insights = analyze_sales(sales_df)

    print("Gerando resumo estratégico com LLaMA 3...")
    summary = summarize_insights(insights)

    print("Resultado final:")
    print(summary)

if __name__ == "__main__":
    run()
