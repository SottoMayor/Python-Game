#! python
# 01 - Utilizando estruturas condicionais faça um programa que pergunte ao
# usuário dois números e mostre:
# A soma deles;
# A multiplicação entre eles;
# A divisão inteira deles;
# Mostre na tela qual é o maior;
# Verifique se o resultado da soma é par ou impar e mostre na tela;
# Se a multiplicação entre eles for maior que 40, divida pelo resultado da
# divisão inteira e mostre o resultado na tela. Se não, mostre que a
# multiplicação não foi maior que 40.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

# Soma
soma = num1 + num2
print(f'{num1} + {num2} = {soma}')

# Multiplicação
multiplicacao = num1 * num2
print(f'{num1} X {num2} = {multiplicacao}')

# Divisão Inteira
divisao_inteira = num1 // num2
print(f'A divisão inteira entre {num1} e {num2} = {divisao_inteira}')

# Buscando o maior
if(num1 < num2):
    print(f'O número {num1} é menor que o número {num2}')
elif(num2 < num1):
    print(f'O número {num2} é menor que o número {num1}')
else:
    print(f'Os números {num1} e {num2} são iguais')

# Soma é ímpar ou par?
print('Essa soma é', 'par' if soma % 2 == 0 else 'impar')

# A multiplicação é maior que 40?
if(multiplicacao > 40):
    print('A multiplicação é maior que 40.')
    if(divisao_inteira != 0):
        resultado = multiplicacao / divisao_inteira
        print('A multiplicação dividida pela divisão inteira dá {resultado}')
    else:
        print('A divisão inteira é 0, e não podemos dividir a multiplicação'
              + 'por 0.')
else:
    print('Opa! A multiplicação não é maior que 40.')
