#! python
def calculadora_notas(nota1, nota2,  nota3):

    if(not(0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10)):
        return print('Notas inválidas, tente novamente!')

    # buscando as notas mais altas
    if(nota1 <= nota2 and nota1 <= nota3):
        # nota1 é a mais baixa
        maior_nota1 = nota2
        maior_nota2 = nota3
        menor_de_todas = nota1
    elif(nota2 <= nota3 and nota2 <= nota1):
        # nota2 é a mais baixa
        maior_nota1 = nota1
        maior_nota2 = nota3
        menor_de_todas = nota2
    else:
        # nota3 é a mais baixa
        maior_nota1 = nota1
        maior_nota2 = nota2
        menor_de_todas = nota3

    media_todas_notas = round((nota1 + nota2 + nota3) / 3, 2)
    print(f'A média com todas as notas seria {media_todas_notas}')

    media_maiores_notas = round((maior_nota1 + maior_nota2) / 2, 2)
    print(f'A média com as maiores notas é {media_maiores_notas}')

    # procurando a maior nota entre as maiores
    if(maior_nota1 > maior_nota2):
        maior_de_todas = maior_nota1
    else:
        maior_de_todas = maior_nota2

    print(f'A maior nota de todas é {maior_de_todas}')

    print(f'A menor nota de todas foi {menor_de_todas}')


n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))

calculadora_notas(n1, n2, n3)
