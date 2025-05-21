import requests
import os
from dotenv import load_dotenv

load_dotenv()

def ask_llm(prompt):
    url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}
    payload = {"inputs": prompt}

    response = requests.post(url, headers=headers, json=payload)

    try:
        result = response.json()
        if isinstance(result, list) and "summary_text" in result[0]:
            resumo = result[0]["summary_text"]
            resposta_final = resumo.split(".")[0] + "."
            return resposta_final
        else:
            return f"Resposta inesperada: {result}"
    except Exception as e:
        return f"Erro ao interpretar resposta: {str(e)}\\nResposta bruta: {response.text}"
