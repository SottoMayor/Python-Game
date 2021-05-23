#! python
# 02 - Utilizando estruturas de repetição com variável de controle, faça um
# programa que receba uma string com uma frase informada pelo usuário e conte
# quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre
# na tela essa mesma frase sem nenhuma vogal.

nome = input('Digite seu nome: ').lower()

vogais = 'aeiou'
# Frequency Counter Pattern Approach
dic_aux = {}

for letra in nome:
    if(letra in vogais):
        dic_aux[letra] = dic_aux[letra] + 1 if letra in dic_aux else 1

print(f'Vogais retiradas: {dic_aux}')

for vogal in vogais:
    nome = nome.replace(vogal, '*')

print(f'Nome sem vogais: {nome}')
