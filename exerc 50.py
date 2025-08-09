""" FAÇA UM PROGRAMA QUE LEIA SEIS NUMEROS INTEIROS E MOSTRE A SOMA DAQUELES QUE FOREM PARES . IMPARES  DESCONSIDERE """
soma = 0
cont = 0
for c in range (1, 7):
    num = int(input(f"Digite o {c} Valor:"))
    if num % 2 == 0 :
        soma  += num
        cont = cont + 1 
print(f"Voce informou \033[31m{cont}\033[0m numeros PARES e a soma é \033[31m{soma}\033[0m")
