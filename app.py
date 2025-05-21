from flask import Flask, request, jsonify
from llm_client import ask_llm
from scraper import scrap_inmet_portal

app = Flask(__name__)

@app.route('/consultar-clima', methods=['POST'])
def consultar_clima():
    try:
        contexto = ["Hoje teremos pancadas de chuva no interior e tempo nublado no litoral."]
        prompt = "Me informe a previsão climática de hoje com base nos dados coletados:\\n\\n" + "\\n".join(contexto)
        resposta = ask_llm(prompt)
        return jsonify({"resposta": resposta})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)