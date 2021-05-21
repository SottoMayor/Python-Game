#! python
from random import randint
from time import sleep
import operator

dicionario = {}

for jogador in range(0, 4):
    jogada = randint(1, 6)
    dicionario[f'{jogador+1}° Jogador'] = jogada


itens = dicionario.items()
print(itens)
itens_ordenado = sorted(itens, reverse=True, key=operator.itemgetter(1))
print(itens_ordenado)

for chave, valor in itens_ordenado:
    sleep(1)
    print(f'O {chave} jogador tirou o valor {valor} ')
