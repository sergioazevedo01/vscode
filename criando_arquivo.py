import csv

dados = [
    ["Nome", "Preço", "Quantidade"],
    ["Camiseta", "10.00", "8",],
    ["tenis", "20.00", "5"],
    ["Chinelo", "60.00", "1"],
    ["Moleton", "170.00", "9"],
    ["Jaqueta", "20.00", "2"],
]

# CRIAR ARQUIVO

with open("dados_pandas.csv", "w", newline="", encoding="utf-8" ) as csvarquivo:
    escritor = csv.writer(csvarquivo)
    escritor.writerows(dados)

