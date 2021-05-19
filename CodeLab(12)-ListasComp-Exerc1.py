#! python
# 01 - Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares
# e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

pares = []  # Essa lista vai receber números pares e ordenados
impares = []  # Essa lista vai receber números impares e ordenados
lista_principal = []  # Essa lista vai receber as listas de pares e impares

for num in range(7):
    numero = float(input(f'Digite o numero {num + 1}: '))

    # Verificar se o número é par ou impar
    if(numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)

# Ordenando as listas
pares_ordenado = sorted(pares)
impares_ordenado = sorted(impares)

lista_principal.append(pares_ordenado)
lista_principal.append(impares_ordenado)

print(lista_principal)
