#! python
dicionario = {}

for numero in range(1, 10):
    if (numero == 2 or numero == 2 or numero == 8):
        continue
    else:
        dicionario[numero] = numero ** 2

print(dicionario)
