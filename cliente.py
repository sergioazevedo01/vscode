
class Cliente :
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade 

    # AO INVES DE EXIBIR O CODIGO DA MEMMORIA, EXIBE O TEXTO ABAIXO
    def __str__(self):
        return f"Cliente(nome={self.nome}, email={self.email}, idade={self.idade})"
    