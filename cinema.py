# exercicio para entra no cinema pela idade 

print("\033[32m-------------------------------------\033[0m")
print("\033[36mBem Vindo ao Cinema Gatoflix \033[0m")
print("\033[32m-------------------------------------\033[0m")
idade = int(input("\033[33mDigite sua Idade : \033[0m"))

# Estrutura de decisão 

if idade < 18 or idade >= 35 :
    print("\033[31mVOCE NÃO PODE ENTRAR NO GATOFLIX\033[0m")
else:
     print("\033[31mVOCE  PODE ENTRAR NO GATOFLIX\033[0m")

""" A ESTRUTURA DE DECISÃO 
IF ->   SE
ELIF -> CASO SE 
ELSE -> CASO CONTRARIO
>   MAIOR
<   MENOR 
>=  MAIOR OU IGUAL
<=  MENOR OU IGUAL
==  IGUALDADE  
"""