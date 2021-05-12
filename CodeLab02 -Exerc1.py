#! python
def imprime_menor(a, b):
    '''
        Essa função recebe dois números e imprime uma mensagem que indica o
        menor entre eles, caso sejam iguais a função indica que são iguais.
    '''

    if(a < b):
        print(f'O número {a} é menor que o número {b}')
    elif(b < a):
        print(f'O número {b} é menor que o número {a}')
    else:
        print(f'Os números {a} e {b} são iguais')


num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

imprime_menor(num1, num2)
