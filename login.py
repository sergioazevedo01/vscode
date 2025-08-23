print("SISTEMA DA ADMINISTRATIVO")

usuario = input("Digite o Usuario ")
senha = input("Digite a senha ")

if usuario == "admin" :
    if senha == "123456" :
        print("Login bem sucedido ")
    else:
        print("Usuario ou Senha incorreta")
else :
    print("Usuario ou Senha incorreta ")

