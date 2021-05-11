#! python
def soma(a, b, c):
    '''
        Essa função recebe 3 números qualquer e printa sua soma.
    '''

    soma_total = a + b + c
    print(f'A soma {a} + {b} + {c} = {soma_total}')


a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

soma(a, b, c)
