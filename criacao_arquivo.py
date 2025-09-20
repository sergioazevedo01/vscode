
import csv   #  xlsx ->  csv

#Criando arquivo CSV 
# Gravando Dados 
dados = [
    ["Nome", "idade", "Cidade"],
    ["Arthur", "58", "Cotia"],
    ["Zago", "16", "Cotia"],
    ["Wishzack", "21", "Cotia"]
]

# Criar CSV 
# nomeArquivo, WRite, novalinha, Codificaçao BR - UTF8
with open("dados.csv", "w", newline="", encoding="utf-8") as csvarquivo: 
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)
# Ler Arquivo 
with open("dados.csv", "r", encoding="utf-8") as csvarquivo:
    leitor = csv.reader(csvarquivo) # Lendo o CSV
    print("Conteudo do Arquivo")
    for linha in leitor:
        print(linha)
