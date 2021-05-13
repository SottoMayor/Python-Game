#! python
nome = input('Digite seu nome: ').lower()

vogais = 'aeiou'

for vogal in vogais:
    print(vogal)
    nome = nome.replace(vogal, '*')

print(nome)
