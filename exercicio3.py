#! python
# 03 - Utilizando estruturas de repetição com teste lógico, faça um programa
# que peça uma senha para iniciar seu processamento, só deixe o usuário
# continuar se a senha estiver correta, após entrar dê boas vindas a seu
# usuário e apresente a ele o jogo da advinhação, onde o computador vai
# “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar
# qual número foi escolhido até acertar, a cada palpite do usuário diga
# a ele se o número escolhido pelo computador é maior ou menor ao que ele
# palpitou, no final mostre quantos palpites foram necessários para vencer.

import random

senha = 'senha_corretinha'

entrada = ''

while(entrada != senha):
    entrada = input('Digite a senha correta: ')

print('Senha correta! Pode entrar!')

tentativas = 0

num_sorteado = random.randint(0, 10)

palpite = -1

while(num_sorteado != palpite):
    palpite = int(input('Qual é seu palpite do número sorteado? '))
    print('Ops, você errou! Tente novamente!')

    if palpite > num_sorteado:
        print('DICA: O número sorteado é menor que seu palpite.')
    elif palpite < num_sorteado:
        print('DICA: O número sorteado é maior que seu palpite.')

    tentativas += 1

print(f'Finalmente você descobriu que {num_sorteado} é o número sorteado,' +
      f' com {tentativas} tentativas!')
