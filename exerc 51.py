"""     PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZAO DE UMA PA 
        NO FINAL MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSA          """




primeiro =int(input("Digite um numero : "))
razao = int(input("Digite a razao : "))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro, decimo + razao, razao):
    print((c), end=(" -> "))
print("\033[31mACABOU\033[0m")
