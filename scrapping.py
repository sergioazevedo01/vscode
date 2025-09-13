# REQUISIÇÃO 
import requests

# RESPONSAVEL POR TRATAR RETORNO 
from bs4 import BeautifulSoup

# pip install requests
# pip install bs4

headers = {
    "User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


url = "https://g1.globo.com/"

resposta = requests.get(url, headers=headers)

# Verificar se deu certo 

if resposta.status_code == 200:
    print("requisicao feita com sucesso ")
    # 200 -> Ok 

    soup = BeautifulSoup(resposta.text, "html.parser")
    # Recortar a informaçao especifica
    noticias = soup.find_all("a", class_="feed-post-link")

    print("Ultimas Noticias:")
    for noticia in noticias:
        print(f'{noticia.text} - {noticia['href']}')

