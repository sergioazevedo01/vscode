
import pandas as pd

import matplotlib.pyplot as plt 

# pip install matplotlib
# pip install pandas 

#  LER O ARQUIVO 

df_csv = pd.read_csv("dados_pandas.csv")

df_filtrado = df_csv[df_csv["Preço"] > 50]
print(df_filtrado)

df_filtrado = df_csv[df_csv["Quantidade"] > 5]
print(df_filtrado)

df_ordenado = df_csv.sort_values(by="Quantidade", ascending=False)
print(df_ordenado) # DO MAIOR PARA O MENOR (DECRESCENTE)

# EXTRAIR ESTATISTICAS 
print(df_csv.describe())

# CRIAR COLUNA FATURAMENTO
df_csv["Faturamento"] = df_csv["Quantidade"] * df_csv["Preço"]
print(df_csv)

# VENDAS
# CAMISETA 70
# CAMISETA 30
# CALCULANDO A MEDIA DE PREÇO DO PRODUTO

media_produto = df_csv.groupby("Nome")["Preço"].mean()
print(media_produto)

#  GRAFICO BOXPLOT
#GRID -> LINHAS 
df_csv.boxplot(column="Preço", by="Nome", grid=True)

plt.title("Distribuiçao de preço por Produto")
plt.xlabel("Preço")
plt.ylabel("Nome")

plt.show()

