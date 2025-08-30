
# SISTEMA DE TAREFAS 
tarefas = []     # LISTA VAZIA 
while True :
    print("===== Menu Tarefas ====")
    print(" 1 - Adicionar Tarefas")
    print(" 2 - Listar Tarefas")
    print(" 9 - Sair do Sitema")

    opcao = input("Escolha sua Opçao : ")

# ADICIONAR TAREFA 

    if opcao == "1" :
        tarefa = input("Digite a nova Tarefa : ")
        
        # APPEND -> ADICIONAR A LISTA
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso !")

    # LISTAR TAREFAS  

    elif opcao == "2" :
        # len -> length -> tamanho

        if len(tarefas) == 0 :
            print(" NAO EXISTEM TAREFAS CADASTRADAS")
        else :
            for tarefa in tarefas :
                print(tarefa)

    elif opcao == "9" :
        print("Saindo do sistema")
        break 
    else:
        print("Opcao nao existente , tente novamente")

