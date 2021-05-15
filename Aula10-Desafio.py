#! python
candidato1 = candidato2 = candidato3 = candidato4 = voto_nulo = voto_branco = 0

voto = 0


while(voto != -1):
    voto = int(input('Digite se se voto vai para 1, 2, 3, ou 4.'
                     + ' Para votar em branco é 5. '))
    if(1 <= voto <= 5 or voto == -1):
        if(voto == 1):
            candidato1 += 1
            print('Voto pra Candidato 1.')
        elif(voto == 2):
            candidato2 += 1
            print('Voto pra Candidato 2.')
        elif(voto == 3):
            candidato3 += 1
            print('Voto pra Candidato 3.')
        elif(voto == 4):
            candidato4 += 1
            print('Voto pra Candidato 4.')
        elif(voto == 5):
            voto_branco += 1
            print('Voto Branco.')
    else:
        print('Você anulou seu voto! ')
        voto_nulo += 1

print('Sessão de votos encerrada! Abaixo vamos aos votos.')
print(f'Candidato 1: {candidato1}, Candidato 2: {candidato2}, Candidato 3:'
      + f' {candidato3}, Candidato 4: {candidato4}')
print(f'Votos brancos: {voto_branco}, votos nulos: {voto_nulo}')
