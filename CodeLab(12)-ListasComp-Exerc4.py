#! python
# 04 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random

lista_jogos = []

quant_jogos = int(input('Quantas combinações você deseja? '))

for combinacao in range(quant_jogos):
    for numero in range(6):
        lista_aleatoria = random.sample(range(1, 61), 6)

    lista_jogos.append(sorted(lista_aleatoria))

print(lista_jogos)
