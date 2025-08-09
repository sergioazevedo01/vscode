""" Programa que vai em sites e recolhe informaçoes """

#requisicoes para os sites 
import requests 

# traduzir a resposta
from bs4 import BeautifulSoup

# url para acesso 
url = "https://g1.globo.com/"

# fazendo busca da requisiçao HTTP
resposta = requests.get(url)

# verificar se a requisiçao deu certo 
if resposta.status_code == 200:
    # 200 -. OK 

    # traduzir a resposta 
    soup = BeautifulSoup(resposta.text, "html.parser")

    print(soup)     # vai escrever o html do site 

# encontrar todas as noticias 
    noticias = soup.find_all("a", class_="feed-post-link")


    print("Ultimas noticias do G1:") 

    # percorrendo todas as noticias 
for index, noticia in enumerate(noticias) : 

    # escrevedo cada noticia 
    print(f"{index+1}.{noticia.text}")