#! python
def nota_conceito(nota):

    '''
        Essa função recebe a nota do aluno(de 0 a 10) e retorna qual foi
        conceito de nota.
    '''

    if(0 <= nota <= 10):
        if(nota <= 4):
            return 'F'
        elif(4 < nota <= 6):
            return 'E'
        elif(6 < nota <= 7):
            return 'D'
        elif(7 < nota <= 8):
            return 'C'
        elif(8 < nota <= 9):
            return 'B'
        elif(nota >= 9):
            return 'A'
    else:
        return 'Nota invalida!'


nota = float(input('Digite uma nota: '))

print(nota_conceito(nota))
