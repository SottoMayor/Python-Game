# 06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa
# sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da
# pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como "Suspeita",
# Entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?"
             ]

controller = 0

print('Você foi acusado de um crime!')
print('Responda sim ou não para as perguntas a seguir.')

for pergunta in perguntas:

    print(pergunta)

    resposta = input('Sim ou Não? ').lower()

    if(resposta == 'sim'):
        controller += 1

print(30*'-')

if(0 <= controller <= 1):
    print('Você está liberado, tudo certo!')
elif(controller == 2):
    print('Você é um suspeito!')
elif(3 <= controller <= 4):
    print('Você é um cúmplice!')
else:
    print('Você é o assassino!')
