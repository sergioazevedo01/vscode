
from controller.cliente_controller import cliente_controller
def exibir_menu():
    print("=== MENU ===")
    print("1 - Cadastrar Cliente ")
    print("2 - Listar Cliente ")
    print("0 - Sair do Sistema ")

def main():
    clienteController = cliente_controller()

    while True :
        exibir_menu()
        opc = input("escolha uma opçao : ")

        if opc == "1":
            nome = input("digite o nome: ")
            email = input("Digite o email: ")
            idade = int(input("Digite a idade : "))
                            
        # SALVAR NO BANCO DE DADOS 
            clienteController.criar_cliente(nome, email, nome)
        elif opc == "2":
            # LISTAR CLIENTES DO BANCO
            clientes = clienteController.listar_cliente()

            for index, cliente in enumerate(clientes, 1):
                print(f"{index}, {cliente}")
        elif opc == 0:
            print("Saindo do Sistema")
            break
        else:
            print("Opçao Invalida")

if __name__ == "__main__":
    main()
