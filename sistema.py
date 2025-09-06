from Models.Pessoa import Pessoa

def menu():
    print("===Menu===")
    print("1 - CRIAR PESSOA")
    print("2 - LISTAR PESSOAS")
    print("3 - LIMPAR LISTA")
    print("9 - sair do sistema")

def iniciarSistema():
    print("Sistema Iniciado")
    pessoas = []                              # CRIAR LISTA DE PESSOAS 

    while (True) :
        menu()
        opcao = input("Selecione uma opçao ... ")
        
        if opcao == "1":
            nome = input("Digite o nome da pessoa ...")
            email = input("Digite o email da pessoa ...")
            pessoa = Pessoa(nome, email)      # MANIFESTANDO A ENTIDADE PESSOA 
            pessoas.append(pessoa)            # ADICIONAR PESSOA A LISTA DE PESSSOAS 
        elif opcao == "2" :
            for pessoa in pessoas :
                print(f'\033[31mNome: {pessoa.get_nome()}, \nEmail: {pessoa.get_email()}\033[m')
                      
            
        

# Logica para iniciar automaticamente 

if __name__ == "__main__" :
    iniciarSistema ()

