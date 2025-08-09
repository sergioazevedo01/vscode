# Biblioteca para criação de Dashboards
import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv("aula_4/vendas_loja.csv")
df["Receita"] = df["Quantidade"] * df["Preço_Unitario"]
df["Data"] = pd.to_datetime(df["data"])
df["Mês"] = df["Data"].dt.to_period("M")

st.title("Dashboard de Vendas")

#Infos principais
st.metric("Total de Vendas", f"R$ {df['Receita'].sum():,.2f}")