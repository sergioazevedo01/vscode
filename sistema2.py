# Sistema gerenciador de nomes 
nomes = []  # lista vazia 

while True :

    print("=== Lista de nomes === ")
    print(" 1- ADICIONAR NOME :")
    print(" 2- Listar Nomes ")
    print(" 3- DELETAR LISTA ")
    print(" 4- deletar nome ")
    print(" 9- Sair do Sistema ")
    

    opcao = input(" Escolha ua opcao : ")

    if opcao == "1" :
        nome = input(" Adicionar Nome : ")
        nomes.append(nome)
        print(" Nome adicionado com sucesso ")
    elif opcao == "2" :
        if len(nomes) == 0 :
            print(" Nao existe nome cadastrado ")
        for nome in (nomes):
            print(nome)
    elif opcao == "3" :
        nomes = []      # ESVAZIA A LISTA 
        print("Lista DELETADA COM SUCESSO")
    elif opcao == "4" :
        if len(nomes) == 0 :
         print("Nome nao encontrado")
        else:
            for posicao, nome in enumerate(nomes):
                print(f"{posicao} {nome}")
            pos = input(" Escolha o nome para deletar : ")
            nomes.remove(nomes[pos])
    elif opcao == "9":
        print("Saindo do Sistema ....")
    else:
        print("Opçao Invalida Tente Novamente")

    

        


