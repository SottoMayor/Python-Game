#! python
import random

tupla = (random.randint(1, 50), random.randint(1, 50), random.randint(
    1, 50), random.randint(1, 50), random.randint(1, 50))

print(f'Essa é a tupla: {tupla}')
print(f'Esse é o maior número da tupla: {max(tupla)}')
print(f'Esse é o menor número da tupla: {min(tupla)}')
