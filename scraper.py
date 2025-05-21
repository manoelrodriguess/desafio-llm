import requests
from bs4 import BeautifulSoup

def scrap_inmet_portal():
    url = 'https://portal.inmet.gov.br/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    cards = soup.select('div.card-body h2.card-title a')
    links = []

    for card in cards[:5]:
        titulo = card.get_text(strip=True)
        href = card.get('href')
        link_completo = f"https://portal.inmet.gov.br{href}" if href and href.startswith('/') else href
        links.append(f"{titulo}\n{link_completo}")

    if not links:
        links.append("⚠️ Nenhum destaque encontrado no site no momento.")

    return links