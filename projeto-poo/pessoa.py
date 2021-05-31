class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 100
        self.estressado = 0
        self.saude = True
        self.contador_academia = 3
        self.fome = True
        self.sujo = True

    def salario(self, recebido):
        if (recebido > 0):
            self.dinheiro += recebido

    def com_sujeira(self, sujeira):
        if(sujeira):
            self.sujo = True
        else:
            self.sujo = False

    def com_fome(self, faminto):
        if(faminto):
            self.fome = True
        else:
            self.fome = False

    def academia(self, foi_malhar=False):
        if(foi_malhar):
            self.contador_academia += 1
            self.com_sujeira(True)
            self.com_fome(True)
        else:
            self.contador_academia -= 2

        if(self.contador_academia <= 0):
            self.saude = False
        else:
            self.saude = True

    def estresse(self, perc_estresse):
        if self.estressado + perc_estresse <= 100:
            self.estressado += perc_estresse
        else:
            self.estressado = 100
        return self.estressado

    def desestresse(self, perc_desestresse):
        if self.estressado - perc_desestresse >= 0:
            self.estressado -= perc_desestresse
        else:
            self.estressado = 0
        return self.estressado

    def dormir(self):
        self.estressado = 0
        self.fome = True
        self.sujo = True

    def __str__(self):
        return f'Status -> {self.nome} está {self.estressado}% estressado!' + \
            ' Além disso ele está ' + ('doente', 'saudável')[self.saude] + \
            ', ' + ('sem', 'com')[self.fome] + ' fome e ' + \
            ('limpo', 'sujo')[self.sujo] + '. O dinheiro em conta é ' + \
            f'R${self.dinheiro}.'
