#! python
import random

tentativas = 0

num_sorteado = random.randint(0, 10)

palpite = -1

while(num_sorteado != palpite):
    palpite = int(input('Qual é seu palpite do número sorteado? '))
    print('Ops, você errou! Tente novamente!')
    tentativas += 1

print(f'Finalmente você descobriu que {num_sorteado} é o número sorteado,' +
      f' com {tentativas} tentativas!')
