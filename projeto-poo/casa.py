from math import floor


class Casa:
    def __init__(self):
        self.comida = 5
        self.preparar_aula = False

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
