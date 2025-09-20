import csv 
import time

ARQUIVO = "produtos.csv"

# ASSIM QUE EXECUTAR ELE VERIFICA SE O ARQUIVO EXISTE E CRIA

try:
    # x -> MODELO UNICO DE CRIAÇAO 
    with open(ARQUIVO, "x", newline="") as arquivo :
        escritor = csv.writer(arquivo)
        escritor.witerow(["Nome", "Quantidade", "Preco"])
except :
    pass # SE JA EXISTE O ARQUIVO ELE SEGUE EM FRENTE 
while True :
    nome = input("Digite o nome do Produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preco: "))
     
# ESCREVER NO ARQUIVO CSV
    with open(ARQUIVO, "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, quantidade, preco])
    print        (f"Produto {nome} adicionado com sucesso ")
    # PERGUNTAR SE DESEJA CONTINUAR O SISTEMA 
    continuar = input("Deseja adicionar outro? (s/n): ")
    if continuar == "n":
        print("Encerrando o sistema...")
        break
      