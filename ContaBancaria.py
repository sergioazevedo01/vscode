class ContaBancaria :
    def __init__(self, saldo) :
        self.saldo = saldo 
    def depositar(self, valor) :
        self.saldo = self.saldo + valor
    def sacar(self, valor) :
        if valor <= self.saldo :
            self.saldo = self.saldo - valor 
            return True
        else :
            return False
    def get_saldo(self) :
        return self.saldo

contaSergio = ContaBancaria(100)

contaSergio.sacar(50)
contaSergio.depositar(50)

print(contaSergio.get_saldo)
