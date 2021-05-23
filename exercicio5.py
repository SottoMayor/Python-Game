# 05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o
# tratamento necessário e retorne o resultado. Depois mostre na tela o
# resultado e a quantidade de letras foram retiradas da frase original.


def maquina_de_vogais(string):
    '''
    Essa função recebe um parâmetro de string, e printa as vogais retiradas,
    a string sem as vogais, e a quantidade de letras retiradas.

    '''

    vogais = 'aeiou'
    counter_stars = 0
    # Frequency Counter Pattern Approach
    dic_aux = {}

    for letra in string:
        if(letra in vogais):
            dic_aux[letra] = dic_aux[letra] + 1 if letra in dic_aux else 1

    print(f'Vogais retiradas: {dic_aux}')

    for vogal in vogais:
        string = string.replace(vogal, '*')

    print(f'String sem vogais: {string}')

    for letra in string:
        if letra == '*':
            counter_stars += 1

    print(f'Quantidade de letras retidadas: {counter_stars}')


nome = input('Digite seu nome: ').lower()
maquina_de_vogais(nome)
