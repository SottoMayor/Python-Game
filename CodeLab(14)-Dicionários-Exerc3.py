#! python
nome = str(input('Digite seu nome: '))
media = float(input('Digite sua média: '))

if 0 <= media <= 10:
    if media < 5:
        situacao = 'Reprovado!'
    elif 5 <= media <= 6.9:
        situacao = 'Recuperação!'
    else:
        situacao = 'Aprovado!'

dicionario = {'nome': nome, 'media': media, 'situacao': situacao}
print(dicionario)
