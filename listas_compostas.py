'''
# Listas compostas são lsitas dentro de listas, com os conceitos
# ensinados anteriormente, nós conseguimos criar a seguinte lista:

pessoa = list()
pessoa.append('Thiago')
pessoa.append(40)

print(pessoa)

# Esse código acima gera um conjunto de dados na mesma lista, porém se eu
# adicionar mais dados de nome e idade na mesma lista, isso pode nos
# confundir na hora de apresentar esses dados ou buscar esses dados.
# Vai ser dificil saber que idade pertence a qual nome, por isso temos as
# listas compostas. Vamos criar uma lista que receba varias listas com nome e
# idade:

# Para criar uma lista composta eu coloco a lista pessoa dentro da lista povo:
povo = list()
# Se eu atribuir sem ess [:] ele cria uma ligação e não uma cópia
povo.append(pessoa[:])

# Agora para adicionar novas listas pessoa dentro da lista povo, eu adiciono
# mais itens nas posições da lista pessoa:

pessoa[0] = 'Maria'
pessoa[1] = 18

# E agora eu adicono a lista pessoa de novo na lista povo:

povo.append(pessoa[:])
print(povo)

# Outra forma de criar listas compostas é:

povoado = [['Thiago', 40], ['Maria', 18], ['José', 34], ['Roberta', 56]]
print(povoado)

# Mostre a lista na posição 0, e o dado na posição 0 dessa lista.
print(povoado[0][0])
# Mostre a lista na posição 0, e o dado na posição 1 dessa lista.
print(povoado[0][1])
# Mostre a lista na posição 1, e o dado na posição 1 dessa lista.
print(povoado[1][1])
# Mostre a lista na posição 3, e o dado na posição 0 dessa lista.
print(povoado[3][0])
# Mostre a lista na posição 2, e o dado na posição 1 dessa lista.
print(povoado[2][1])

# Vamos utilizar o for para varrer essa lista:

for p in povoado:
    print(p[0])  # Mostra apenas os nomes dessas listas.
    print(f'{p[0]} tem {p[1]} anos de idade.')


# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes,
# utilizando o for e o if, verifique quais clientes são maiores de idade
# e quais são menores de idade e mostre na tela a seguinte frase para cada
# um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e
# também quantos são maiores e quantos são menores de idade.

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()  # Limpa a lista dados

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
'''
# Exercicio de fixação

# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em
# uma lista, depois do dado inserido, pergunte ao usuário se ele quer
# continuar, se ele não quiser pare o programa. No final mostre:
# Quantas pessoas foram cadastradas
# Mostre o maior peso
# Mostre o menor peso

quantidade = int(input('Quantas pessoas serão entrevistadas? '))

print('Digite o nome da pessoa, aperte enter e digite o peso(kg) da pessoa!')

# sistema para adicionar pessoas na lista(listas aninhadas)
pessoas = [[(input('Nome da Pessoa: ') if x == 0
            else input('Peso(kg) da pessoa: ')) for x in range(2)]
           for y in range(quantidade)]

print(f'O número de pessoas cadastradas são: {len(pessoas)}')

# buscando o maior e o menor número dentro os pesos
maior = 0
menor = 1000
for pessoa in pessoas:
    if(float(pessoa[1]) > maior):
        maior = float(pessoa[1])
    if(float(pessoa[1]) < menor):
        menor = float(pessoa[1])

print(f'O maior peso foi: {maior}')
print(f'O menor peso foi: {menor}')
