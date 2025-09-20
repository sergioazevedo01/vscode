
import pandas as pd
import matplotlib.pyplot as plt 

import streamlit as st
# PIP INSTALL STREAMLIT

# UPLOAD DO ARQUIVO CSV
arquivo = st.file_uploader("Envie seu arquivo CSV", type=["csv"])

# VERIFICAR SE O ARQUIVO EXISTE

if arquivo is not None:
# LER O ARQUIVO 
    df = pd.read_csv(arquivo)
    st.write("Dados carregados :")
    st.dataframe(df)

# SELECTBOX - PARA TIPO DE GRAFICO 
    opcao = st.selectbox(
        "Escolha o tipo de Grafico : ", 
        ["Barras", "Pizza", "Linha"]
    )

    # GRAFICO DE BARRAS 
    if opcao == "Barras":
        st.bar_chart(df.set_index("Nome")["Quantidade"])

    # GRAFICO DE LINHAS
    elif opcao == "Linhas":
        st.line_chart(df.set_index("Nome")["Quantidade"])

    # GRAFICO DE PIZZA 
    elif opcao == "Pizza":
        st.pyplot(df.set_index("Nome").plot.pie(y="Quantidade").figure)

else:
    st.info("Envie um arquivo csv com as colunas Nome e Quantidade....")

#python -m streamlit run graficos_stream.py (COMANDO)

