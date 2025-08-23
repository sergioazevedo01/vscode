# Solicite o nome e senha do Usuario 

# Logo em seguida realize os prints com as informaçoes

nome = input("Digite seu nome : " )
email = input(" Digite seu email ; ")
senha = input("Digite sua senha : ")

if nome.strip() == "":
    print("Nome nao foi preechido")
    
print(" \033[31mO nome do usuario\033[0m ", (nome), "\n \033[31mO email é :\033[0m", (email), "\n \033[31mSenha do usuario :\033[0m ", (senha) )
