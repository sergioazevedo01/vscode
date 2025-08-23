

print("BEM VINDO AO BANCO Girabank")
saldo = float(input(" DIGITE SEU SALDO ... R$ : "))
transferencia = float(input("QUAL O VALOR DA TRANSFERENCIA ? R$ : "))

# VALIDE SE A PESSOA POSSU SALDO SUFICIENTE PARA TRANSFERENCIA 

if saldo < transferencia :
    print(" SALDO INSUFICIENTE ")
elif transferencia == saldo :
    print(" SUA CONTA VAI FICAR ZERADA !")
else :
    saldo = saldo - transferencia 
    print(f" Seu saldo atual é de : {saldo:.2f}")


