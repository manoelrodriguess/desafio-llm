# API de Clima com LLM e Flask (compatível com Postman)

Este projeto usa um modelo compatível com contas gratuitas da Hugging Face (sem erros de permissão).

## Modelo usado:
https://huggingface.co/mrm8488/t5-base-finetuned-common_gen

## Como usar:

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Coloque seu token Hugging Face no `.env`:
```
HF_TOKEN=hf_seutokenaqui
```

3. Inicie o Flask:
```bash
python app.py
```

4. No Postman:
- Método: POST
- URL: http://localhost:5000/consultar-clima
- Body (raw, JSON):
```json
{
  "prompt": "Explique o contexto climático abaixo:"
}
```