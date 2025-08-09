import pandas as pd
import matplotlib as plt

# Ler csv
df = pd.read_csv("aula_4/vendas_loja.csv")

# nome das colunas
#criar coluna chamada receita
df["Receita"] = df["Quantidade"] * df["Preço_unitário"]

# sum -> soma
total_receita = df["Receita"].sum()

total_receita2 = df["Receita"] # Total por produto
print(total_receita2)

print("Total de vendas R$", total_receita) # Total de receita faturado

# Produto mais vendido em quantidade 
produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax()

