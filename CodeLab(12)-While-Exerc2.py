#! python
# 02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:

#  A) quantas pessoas tem mais de 18 anos.
#  B) quantos homens foram cadastrados.
#  C) quantas mulheres tem menos de 20 anos.

informacoes = []

while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (M-F): ').strip().upper()

    informacoes.append((idade, sexo))

    continuar = input('Deseja continuar (S-N): ').strip().upper()
    if(continuar == 'N'):
        break

de_maior = 0
homens = 0
mulheres_menor_20 = 0

for info in informacoes:
    if(info[0] >= 18):
        de_maior += 1
    if(info[1] == 'M'):
        homens += 1
    if(info[1] == 'F' and info[0] < 20):
        mulheres_menor_20 += 1

print(50*'-')

print(f'Pessoas maiores de idade: {de_maior}')
print(f'Quantidade de homens: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheres_menor_20}')
