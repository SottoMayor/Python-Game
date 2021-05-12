#! python
import datetime


def voto(ano_nascimento):

    '''
        Essa função recebe o ano de nascimento do cidadão e retorna se ele
        não pode votar, pode votar ou é obrigado a votar.
    '''

    hoje = str(datetime.date.today())
    ano_atual = int(hoje[:4])

    idade = ano_atual - ano_nascimento

    print(idade)

    if(idade < 16):
        return 'NEGADO'
    elif(16 <= idade < 18):
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


ano_nascimento = int(input('Digite o ano de seu nascimento: '))

print(voto(ano_nascimento))
