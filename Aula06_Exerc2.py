#! python
def verificacao(numero):

    '''
        Essa função recebe um número qualquer e retorna "P" se for positivo,
        "N" se for negativo ou "0" se for 0.
    '''

    if numero > 0:
        return 'P'
    elif numero < 0:
        return 'N'
    else:
        return '0'


num = float(input('Digite um número: '))

print(verificacao(num))
