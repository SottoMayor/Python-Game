#! python
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
num4 = int(input('Digite um número: '))

tupla = (num1, num2, num3, num4)

contador_9 = 0

# print(tupla.count(9))
for numero in tupla:
    if(numero == 9):
        contador_9 += 1

print(contador_9)

print(tupla.index(3))
