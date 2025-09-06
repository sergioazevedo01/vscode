
class Carro :

# Configuracao inicial do Objeto

    def __init__(self, nome, cor, modelo, ano, marca) :
        #Definir atributo 
        self.nome = nome
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

    def correr(self) :
        print("Correndo muito .......")

    def frear(self) :
        print("Freiando ...... pastilha esta ruim ......")

    def ligar(self) :
        print("Ligando o carro...., self.nome .....")
              
passatiCarro = Carro("passati", "preto", "v1", "2025", "bmw")
passatiCarro.ligar()
passatiCarro.correr()
passatiCarro.frear()
