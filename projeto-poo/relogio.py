class Relogio:
    def __init__(self):
        self.horas = 7
        self.minutos = 0
        self.dia = 1

    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
        if(self.horas >= 24):
            self.horas = 0
            self.minutos = 0

    def atrasado_presencial(self):
        return (self.horas > 12 or (self.horas == 12 and self.minutos > 0))

    def atrasado_EAD(self):
        return (self.horas > 19 or (self.horas == 19 and self.minutos > 0))

    def __str__(self):
        if (0 <= self.minutos <= 9):
            return f"Relógio -> {round(self.horas)}:0{round(self.minutos)}" + \
                f"h do dia {self.dia}"
        else:
            return f"Relógio -> {round(self.horas)}:{round(self.minutos)}" + \
                f"h do dia {self.dia}"
