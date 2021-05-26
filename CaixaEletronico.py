#! python
'''
Crie uma classe chamada Conta para simular as operações de uma conta corrente.
Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e
Depositar. Crie um objeto da classe Conta e teste os atributos e métodos
implementados.​ Adicione uma regra no método Sacar, onde o usuário só poderá
sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na
tela: "Você não tem saldo suficiente para essa operação.'
'''


class Conta:
    # constutor
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    # métodos
    def sacar(self, valor_saque):
        if self.saldo - valor_saque >= 0:
            self.saldo = self.saldo - valor_saque
        else:
            print(f'O seu saldo R${self.saldo} é insulficiente para o saque de'
                  + f' R${valor_saque}')
        return self.saldo

    def depositar(self, valor_deposito):
        self.saldo = self.saldo + valor_deposito
        return self.saldo

    def __str__(self):
        return f'Seu saldo é de R${self.saldo}.'
