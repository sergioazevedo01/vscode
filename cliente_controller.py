
from models.cliente import Cliente 
from database.database import BancoFake

class cliente_controller :
    def __init__(self):
        # CONEXAO COM BANCO 
        self.database = BancoFake()

    def criar_cliente(self, nome, email, idade):
        # CRIAR OBJETO CLIENTE 
        novo_cliente = Cliente(nome, email, idade)

        # CONVERTENDO PARA DICT -> JSON
        dict_cliente = {
            "nome" : novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade
        }
        
        self.database.adicionar_cliente(dict_cliente)
        print("Cliente cadastrado com sucesso")

    def listar_cliente(self):
        """
        Retornar uma lista com todos os clientes 
        """
        return self.database.listar_clientes()
    
