#! python
# 01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.
# (utilizar while sem break)

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

comando = int(input('''
-> Digite uma dessas opções:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
-------------> '''))

while comando != 5:
    if(1 <= comando <= 5):

        print('\n')

        if comando == 1:
            print(f'{num1} + {num2} = {num1 + num2}')
        elif comando == 2:
            print(f'{num1} X {num2} = {num1 * num2}')
        elif comando == 3:
            print(f'O maior é: {num1 if num1 > num2 else num2}')
        elif comando == 4:
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite outro número: "))

        comando = int(input('''
-> Digite uma dessas opções:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
-------------> '''))
    else:
        print('Tente novamente! A opção escolhida é inválida =(')
        comando = int(input('''
-> Digite uma dessas opções:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
-------------> '''))

print('Até logo!')
