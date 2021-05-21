#! python

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente
# de 0, o dicionário receberá também o ano de contratação e o salário. Calcule
# e acrescente , além da idade , com quantos anos a pessoa vai se aposentar.
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.​​

dicionario = {}

dicionario['nome'] = input('Digite seu nome: ')
dicionario['ano_nascimento'] = int(input('Digite seu ano de nascimento: '))
dicionario['carteira_trabalho'] = int(input('Digite seu número de CT: '))

if dicionario.get('carteira_trabalho', 0) != 0:
    dicionario['ano_contratacao'] = int(
        input('Digite seu ano de contratação: '))
    dicionario['salario'] = float(input('Digite o seu salário: '))
    dicionario['ano_aposentar'] = dicionario.get('ano_contratacao') + 35

print(dicionario)
