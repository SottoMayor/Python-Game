from math import floor


class Casa:
    def __init__(self):
        self.comida = 5
        self.preparar_aula = False

    def consumo(self):
        if self.comida > 0:
            self.comida -= 1
        else:
            self.comida = 0

    def mercado(self, dinheiro):
        preco_alimento = 20
        qtt_alimento = floor(dinheiro / preco_alimento)
        troco = dinheiro % preco_alimento
        dinheiro = troco
        self.comida += qtt_alimento

    def preparacao_aula(self, preparada):
        if(preparada):
            self.preparar_aula = True
        else:
            self.preparar_aula = False

    def __str__(self):
        return f'Casa -> Você tem {self.comida} quantidade de ' +\
            'comidas e você ' + ('não ', '')[self.preparar_aula] +\
            'preparou a aula.'


casa = Casa()
print(casa)
casa.preparacao_aula(True)
print(casa)