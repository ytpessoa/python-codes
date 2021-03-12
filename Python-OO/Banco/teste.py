# from arquivo import Classe
from clientes import Cliente
from contas import Conta
from banco import Banco


joao = Cliente("Joao da Silva", "777-1234")
maria = Cliente("Maria Silva", "888-999")
jose = Cliente("Jose da Silva", "1010-1010" )

contaJM = Conta([joao, maria], 100)
contaJ = Conta([jose], 10)

tatuBanco = Banco("Tatú")
tatuBanco.abre_conta(contaJM)
tatuBanco.abre_conta(contaJ)
print(f"Lista de Contas: {tatuBanco.lista_contas()}")
# print(conta1.resumo())
# print(conta1, conta1.extrato())

# print(conta2.resumo())
# print(conta2, conta2.extrato())



