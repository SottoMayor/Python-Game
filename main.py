#! python
from CaixaEletronico import Conta

cliente = Conta('Vanessa', 1)

print(cliente.sacar(0))
print(cliente.depositar(100))
print(cliente)
