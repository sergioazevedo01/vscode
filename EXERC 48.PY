# FÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SAO MULTIPLOS DE 3 E QUE SE ENCONTRAM NO 
# INTERVALO DE 1 ATE 500
soma = 0
cont = 0 
for c in range(1, 501, 2):
    if c % 3 == 0:
     soma += c
     cont = cont + 1
print(f"\033[31mForam {cont} numeros processados\033[0m")
print(f"\033[31mA Soma de todos é : {soma}\033[0m")