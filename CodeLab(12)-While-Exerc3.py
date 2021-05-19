# 03 - Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

compras = []

while True:
    nome_produto = input('Nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Digite a quantidade: '))

    preco_total = preco * quantidade

    compras.append((nome_produto, preco_total))

    continuar = input('~~~ Você deseja continuar? (S-N) ~~~ ').strip().upper()

    if continuar == 'N':
        break

total_gasto = 0
produtos_acima_1000 = 0
produto_mais_barato_nome = compras[0][0]
produto_mais_barato_preco = compras[0][1]

for compra in compras:
    total_gasto += compra[1]

    if compra[1] > 1000:
        produtos_acima_1000 += 1

    if compra[1] < produto_mais_barato_preco:
        produto_mais_barato_nome = compra[0]
        produto_mais_barato_preco = compra[1]


print(50*'-')

print(f'O total gasto foi: {total_gasto}')
print(f'A quantidade de produtos acima de 1000 foi: {produtos_acima_1000}')
print(f'O produto mais barato comprado foi: {produto_mais_barato_nome}')
