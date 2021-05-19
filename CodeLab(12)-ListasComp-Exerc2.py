#! python
# 02 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha
# com valores lidos pelo teclado. No final, mostre a matriz na tela, com
# essa formatação:
"""
[  1  ][  2  ][  3  ]
[  4  ][  5  ][  6  ]
[  7  ][  8  ][  9  ]

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[coluna][linha])
"""

# lista = [float(input('Digite um numero: ')) for x in range(9)]

lista = []
for x in range(9):
    num = float(input('Digite um numero: '))
    lista.append(num)

for linha in range(3):  # 0, 1, 2
    print('\n')
    for coluna in range(3):  # 0, 1, 2
        print(f'[ {lista[ (linha+coluna) + (2*linha) ]} ]', end=' ')
print('\n')
