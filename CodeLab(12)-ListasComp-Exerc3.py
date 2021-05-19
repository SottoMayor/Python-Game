#! python
# 03 - Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

lista = [float(input('Digite um numero: ')) for x in range(9)]

for linha in range(3):  # 0, 1, 2
    print('\n')
    for coluna in range(3):  # 0, 1, 2
        print(f'[ {lista[ (linha+coluna) + (2*linha) ]} ]', end=' ')
print('\n')

# soma dos números pares da matriz
lista_pares = [num for num in lista if num % 2 == 0]
print(f'A soma dos números pares da matriz: {sum(lista_pares)}')

# soma dos números da 3° coluna da matriz
lista_3coluna = [lista[num] for num in range(9) if (num + 1) % 3 == 0]
print(f'A soma dos números da 3° coluna da matriz: {sum(lista_3coluna)}')

# O maior número da 2° linha
maior_2linha = max(lista[3:6])
print(f'O maior número da 2° linha é {maior_2linha}')
