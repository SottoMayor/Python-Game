#! python
def maior_que_limite(a, b, limite):
    '''
        Essa função recebe 3 parâmetros, os primeiros 2 serão somados e
        comparados com o 3°. Se a soma for maior que o 3° parâmetro a
        função retorna True, senão retorna False
    '''

    soma = a + b

    return True if soma > limite else False


num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
limite = float(input("Digite um número como limite: "))
print(maior_que_limite(num1, num2, limite))
