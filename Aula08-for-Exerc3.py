#! python
numeral = int(input('Digite um número: '))

for numero in range(1, numeral+1):
    if(numeral % numero == 0):
        print(f'{numero} é divisor de {numeral}')
