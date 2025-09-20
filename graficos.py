import pandas as pd
import matplotlib.pyplot as plt

# PIP INSTALL PANDAS 
# PIP INSTALL MATPLOTLIB

ARQUIVO = "produtos.csv"
CAMPOS = ["Nome", "Quantidade", "Preco"]

df = pd.read_csv(ARQUIVO, encoding="utf-8")

df["Faturamento"] = df["Quantidade"] * df["Preco"]
print(df)

df.boxplot(column="Preco", by="Nome", grid=True)
plt.title("Distribuicao de preco por Nome")
plt.xlabel("Preco")
plt.ylabel("Nome")

plt.show()

df.plot(kind="area", x="Nome", y="Preco", grid=True)
plt.title("Preco dos Produtos")
plt.xlabel("Preco")

plt.show()

