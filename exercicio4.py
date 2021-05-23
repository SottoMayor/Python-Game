# 04 - Utilizando funções e listas faça um programa que receba uma data no
# formato DD/MM/AAAA e devolva uma string no formato DD de mesPorExtenso de
# AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja
# inválida.

def converte_data(data):
    '''
        Essa função recebe uma string com a data do tipo DD/MM/AAAA e
        retorna a data passada na forma "Dia DD do mês MM do ano de AAAA"
    '''

    # 24/10/2000

    dia = int(data[0:2])  # 24
    mes = int(data[3:5])  # 10
    ano = int(data[6:])  # 2000

    if(not(0 <= dia <= 31 and 0 <= mes <= 12 and ano >= 0)):
        return 'Data Inválida!'

    # Verificando se o ano é bissexto
    bissexto = False

    if(ano % 100 == 0):
        if(ano % 400 == 0):
            bissexto = True
    elif(ano % 4 == 0):
        bissexto = True

    if(mes == 1):
        mes = 'Janeiro'
    elif(mes == 2):
        if(dia <= 28):
            mes = 'Fevereiro'
        elif(dia == 29 and bissexto):
            mes = 'Fevereiro'
        else:
            return 'Data inválida!'
    elif(mes == 3):
        mes = 'Março'
    elif(mes == 4):
        mes = 'Abril'
    elif(mes == 5):
        mes = 'Maio'
    elif(mes == 6):
        mes = 'Junho'
    elif(mes == 7):
        mes = 'Julho'
    elif(mes == 8):
        mes = 'Agosto'
    elif(mes == 9):
        mes = 'Setembro'
    elif(mes == 10):
        mes = 'Outubro'
    elif(mes == 11):
        mes = 'Novembro'
    elif(mes == 12):
        mes = 'Dezembro'

    return f'Dia {dia} do mês {mes} do ano de {ano}'


data = input('Digite uma data do tipo DD/MM/AAAA: ')
print(converte_data(data))
