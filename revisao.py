"""   REVISAO DA AULA 1 DE PYTHON   """

print("Bem vindo ao Sistema")
print("Digite se voce é maior de idade")
valor = float(input("Digite 1 para maior e 0 para menor : "))

if valor == 1 :
    print(" \033[31mPode assistir o Gatoflix\033[0m ")
elif valor == 0 :
    print(" \033[31mSorry Voce é menor de idade\033[0m ")
else:
    print(" \033[33mOPÇAO INVALIDA\033[0m  ")

