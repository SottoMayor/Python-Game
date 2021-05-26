class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.dinheiro = 0
        self.salario = 100

    def __str__(self):  # Pesquisar significado dessa função especifica.
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+(
            "com" if self.fome else "sem")+" fome e "+(
                "" if self.medicado else "não "
                )+"tomou sua medicação. Você tem "+str(
                    self.dinheiro)+" reais na sua conta."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.medicado = False
