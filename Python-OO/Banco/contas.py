

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = saldo #opcional, se não passar inicia com 0
        self.clientes = clientes #lista de objetos
        self.numero = numero #string
        self.operacoes = [] #lista

    
    def resumo(self):
        print(f"CC: {self.numero}, Saldo: {self.saldo}")
    
    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])
    
    def extrato(self):
        for o in self.operacoes:
            print(f"{o[0]} - {o[1]}")
        print(f"SALDO: {self.saldo}")
