import os
import httpx

def summarize_insights(insights: dict) -> str:
    prompt = (
        "Você é um analista sênior de dados de e-commerce. Com base nos seguintes dados, gere um resumo estratégico em português, "
        "utilizando linguagem de negócios, destacando oportunidades ou alertas:\n\n"
        f"- Faturamento total: R$ {insights['total_revenue']:.2f}\n"
        f"- Receita média diária: R$ {insights['avg_daily_revenue']:.2f}\n"
        f"- Produto com maior receita: {insights['top_product']}\n"
        f"- Dia com maior faturamento: {insights['top_day']}\n\n"
        "Gere uma análise profissional em, no máximo, um parágrafo de 500 caracteres."
    )

    response = httpx.post(
        f"{os.getenv("HOST_LLM")}/api/generate",
        json={
            "model": "llama3.1:latest",
            "prompt": prompt,
            "stream": False
        },
        timeout=3600
    )

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return f"Erro ao gerar resumo com LLaMA 3: {response.text}"
