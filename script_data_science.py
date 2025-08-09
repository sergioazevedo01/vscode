#
import numpy as np

# ESTATISTICAS
from statistics import mode 

# SEQUENCIA NUMERICA 
dados = [10, 12, 10, 14, 14, 15, 20]

# MEDIA
media = np.mean(dados)

# MEDIANA -> vALOR cENTRAL, ROBUSTO CONTRA OUTLIERS
mediana = np.median(dados)

# MODA -> VALOR MAIS FREQUENTE 
moda = mode(dados)

#DESVIO PADRAO -> DISPERSAO DE DADOS 
desvio_padrao = np.std(dados)

# VARIAÇIA -> QUADRADO DE DESVIO PADRAO 
variancia = np.var(dados)
