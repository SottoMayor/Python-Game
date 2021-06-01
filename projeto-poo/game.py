from casa import Casa
from pessoa import Pessoa
from relogio import Relogio

from random import randint


def aleatorios_multiplos_5(lim_inf=1, lim_sup=100):
    '''
    Essa função recebe dois argumentos inteiros, o limite inferior e
    superior de um intervalo, e gera uma lista com multiplos de 5.
    Ela retorna um número aleatório dessa lista.
    '''
    # Gerando a lista de multiplos de 5
    lista = [num for num in range(lim_inf, lim_sup + 1) if num % 5 == 0]
    # Escolhendo um índice aleatório
    index = randint(0, len(lista) - 1)
    # Escolhendo aletoriamente um número na lista
    resultado = lista[index]
    return resultado


if __name__ == '__main__':

    print('\nBem-vindo ao jogo da vida! Desenvolvido por David Sotto, ' +
          'Eduardo Henrique, Francisco Chagas.\n')

    print("-*-" * 50)

    print('\nVocê é um professor de matemática, durante o dia voce tomará ' +
          'decisões, onde haverá consequências.')
    print('A cada decisão tomada, haverá um consumo de tempo.')

    print("-*-" * 30)

    print('\nLembre-se que sua rotina sera bem corrida, lembre-se que sua ' +
          'é primordial, para executar as taferas do dia.')

    print("-*-" * 30)

    print('\nO personagem dá 2 aulas por dia, sendo uma 1 presencial ' +
          '[12h-15h] e outra EAD [19h-22h].')
    print('Ir trabalhar é importante para ganhar dinheiro!')

    print("-*-" * 30)

    print('\nAlgumas situações deixam o personagem estressado! Por isso é ' +
          'importante fazer atividades relaxantes, como ir pra academia ou ' +
          'mexer no celular.')
    print('Se o estresse estiver acima de 70%, o rendimento do personagem ' +
          'cair consideravelmente.')

    print("-*-" * 30)

    print('\nPara manter um nível de saúde ideal, vá para academia, exercícios'
          + ' mantém sua saúde 100%.')
    print('Academia te mantem saudável, além de reduzir seus níveis de ' +
          'estresse.')

    print("-*-" * 30)

    print('\nSeu personagem fica com fome, alimente ele 3 vezes ao dia. Senão,'
          + ' os níveis de estresse vão subir e sua saúde será prejudicada.')

    print("-*-" * 30)

    print('\nLembre-se de fazer a higiêne pessoal a cada atividade. ' +
          'Isso vai te ajudar a manter os níveis de saúde e estresse ' +
          'controlados.')

    print("-*-" * 30)

    nome = input('Qual será o nome do seu personagem? ')

    print('')
    personagem = Pessoa(nome)
    relogio = Relogio()
    casa = Casa()

    print(personagem)
    print(relogio)
    print(casa)

    while True:
        print("=" * 100)
        # Dicas para ir trabalhar presencial
        if(relogio.horas < 11):
            print('\nVocê tem que trabalhar às 12h, então saia de casa antes '
                  + 'das 11h. Não esqueca de preparar sua aula, antes de sair '
                  + 'de casa!\n')
        elif(11 <= relogio.horas < 12):
            print('Já passou das 11h, você poderá se atrasar! Saia agora para'
                  + ' ir trabalhar.')
        elif(12 <= relogio.horas < 15):
            print('Você está atrasado! Vá trabalhar agora!.')

        # Dicas para ir trabalhar EAD
        if(17 <= relogio.horas <= 18):
            print('\nVocê tem que trabalhar às 19h, não esqueça de '
                  + 'preparar a aula e cuidado para não se atrasar! ')
        elif(19 <= relogio.horas < 22):
            print('Você está atrasado! Vá trabalhar agora!.')

        # Ações que o personagem pode fazer
        print("\nAções:")
        print("1 - Tomar banho e escovar os dentes")
        print("2 - Se alimentar")
        print("3 - Pedir um ifood")
        print("4 - Dar uma soneca")
        print("5 - Ir à academia")
        print("6 - Jogar video game")
        print("7 - Mexer no celular")
        print("8 - Ir ao mercado")
        print("9 - Preparar a aula")
        print("10 - Ir trabalhar[presencial]")
        print("11 - Ir trabalhar[EAD]")
        print("0 - Sair do jogo")
        opcao = int(input("Escolha sua ação: "))
        print("")
        # Validação de ações
        if(0 <= opcao <= 11):
            # Tomar banho e escovar os dentes
            if(opcao == 1):
                personagem.com_sujeira(False)
                relogio.avancaTempo(20)
            # Se alimentar
            elif(opcao == 2):
                if casa.comida > 0:
                    personagem.com_fome(False)
                    relogio.avancaTempo(45)
                    casa.consumo()
                else:
                    print('Você está sem comida em casa!')
                    print('Para comer peça um ifood ou vá ao mercado.\n')
                    personagem.estresse(30)
                    relogio.avancaTempo(20)
            #  Pedir um ifood
            elif(opcao == 3):
                PRECO_ALIMENTO = 25
                # Verificando se o personagem tem dinheiro para
                # fazer o pedido
                if(personagem.dinheiro >= PRECO_ALIMENTO):
                    personagem.dinheiro -= PRECO_ALIMENTO
                    relogio.avancaTempo(75)
                else:
                    print(f'O valor do alimento é R${PRECO_ALIMENTO} e você ' +
                          f'só possui R${personagem.dinheiro}.'
                          )
                    print('Saldo insulficiente!')
                    personagem.estresse(50)
                    relogio.avancaTempo(30)
            # Dar uma soneca
            elif(opcao == 4):
                duracao_soneca = aleatorios_multiplos_5(1, 100)
                print(f'Você tirou uma soneca de {duracao_soneca} minutos.')
                relogio.avancaTempo(duracao_soneca)
                perc_desestresse = int((duracao_soneca/100) * 100)
                personagem.desestresse(perc_desestresse)
            # Ir à academia
            elif(opcao == 5):
                personagem.academia(True)
                personagem.desestresse(70)
                print('Você foi à academia! E gastou 15 min de caminhada.')
                relogio.avancaTempo(105)
            # Jogar video game
            elif(opcao == 6):
                duracao_game = aleatorios_multiplos_5(30, 175)
                print(f'Você passou {duracao_game} minutos jogando video ' +
                      'game.')
                relogio.avancaTempo(duracao_game)
                perc_desestresse = int((duracao_game/175) * 100)
                personagem.desestresse(perc_desestresse)
            # Mexer no celular
            elif(opcao == 7):
                duracao_celular = aleatorios_multiplos_5(1, 60)
                print(f'Você passou {duracao_celular} minutos mexendo no ' +
                      'celular.')
                relogio.avancaTempo(duracao_celular)
                perc_desestresse = int((duracao_celular/60) * 100)
                personagem.desestresse(perc_desestresse)
            # Ir ao mercado
            elif(opcao == 8):
                print('No mercado cada alimento custa R$20, e você tem ' +
                      f'R${personagem.dinheiro}')
                dinheiro_mercado = float(input('Quanto você deseja gastar? '))
                # Verificando se a entrada é menor ou igual ao dinheiro
                # disponível
                if dinheiro_mercado <= personagem.dinheiro:
                    personagem.dinheiro += casa.mercado(dinheiro_mercado) \
                        - dinheiro_mercado
                    print(f'Agora você tem R${personagem.dinheiro} em conta.')

                    personagem.estresse(30)
                    transito = aleatorios_multiplos_5(20, 100)
                    relogio.avancaTempo(150 + transito)
                    print('\nVocê passou 150 min fazendo as compras e pegou ' +
                          f'{transito} min de transito.')
                else:
                    print(f'Você não consegue gastar R${dinheiro_mercado}, ' +
                          f'pois você possui apenas R${personagem.dinheiro}.')
                    personagem.estresse(60)
                    transito = aleatorios_multiplos_5(20, 100)
                    relogio.avancaTempo(150 + transito)
                    print('\nVocê não comprou nada, perdeu 150 min fazendo ' +
                          f'compras e {transito} min de transito.')
            # Preparar a aula
            elif(opcao == 9):
                casa.preparacao_aula(True)
                print('Você preparou sua aula!')
                relogio.avancaTempo(30)
            # Ir trabalhar[presencial]
            elif(opcao == 10):
                # O Salário é a diária por aula
                SALARIO = 200
                # A penalidade é acumulativa e desconta no salário.
                PENALIDADE = 0
                # Validando horário em que o personagem pode dar a aula
                if(10 <= relogio.horas < 15):
                    # Penalidade se o personagem está muito estressado
                    if(personagem.estressado >= 70):
                        print('Você foi dar a aula muito estressado,' +
                              'e acabou xingando o diretor! Por isso, ' +
                              'recebeu uma multa de 20% de redução do salário.'
                              )
                        PENALIDADE += 20/100
                    # Penalidade se o personagem está sujo
                    if(personagem.sujo):
                        print('Você foi dar a aula fedendo a cecê! Isso ' +
                              'incomodou bastante, e você foi penalizado com '
                              + 'de 10% do salário.'
                              )
                        PENALIDADE += 10/100

                    # Penalidade se o personagem está com fome
                    if(personagem.fome):
                        print('Você foi dar a aula com fome, e seu rendimento '
                              + 'abaixo do esperado! Você foi penalizado com '
                              + 'de 10% do salário.'
                              )
                        PENALIDADE += 10/100
                    # Penalidade se o personagem não preparou a aula
                    if(not(casa.preparar_aula)):
                        print('Você não preparou a aula, nesse caso seu ' +
                              'rendimento não foi satisfatório, por isso ' +
                              'sofrerá uma penalidade de redução de 30% ' +
                              'do salário')
                        PENALIDADE += 30/100
                    # Descontando as penalidades no salário
                    SALARIO += -SALARIO*PENALIDADE

                    # Verificando se o personagem está atrasado
                    if (12 <= relogio.horas < 15):
                        atraso_horas = relogio.horas-12
                        atraso_minutos = relogio.minutos
                        salario_atraso = round((
                            180-(atraso_horas*60 + atraso_minutos)
                        ) * SALARIO/180, 2)
                        print(f'Você está atrasado em {atraso_horas}h e ' +
                              f'{atraso_minutos} min.')
                        print('A cada aula(3h trabalhadas) você recebe R$200, '
                              + 'descontando todas as penalidades você recebeu'
                              + f' {salario_atraso}')
                        horario_saida = 180-(atraso_horas*60 + atraso_minutos)

                        personagem.salario(salario_atraso)
                        personagem.estresse(70)
                        transito = aleatorios_multiplos_5(35, 120)
                        relogio.avancaTempo(horario_saida + transito)

                        print(f'Você saiu as 15h da aula e pegou {transito} '
                              + 'min de trânsito')

                    else:
                        print('Você chegou no horário certo, vamos trabalhar!')
                        print(f'Você ganhou R${SALARIO} reais!')
                        personagem.salario(SALARIO)
                        personagem.estresse(35)
                        transito = aleatorios_multiplos_5(35, 120)
                        hora_saida = 14 - relogio.horas
                        minutos_saida = 60 - relogio.minutos
                        horario_saida = 60*hora_saida + minutos_saida

                        relogio.avancaTempo(horario_saida + transito)

                        print(f'Você saiu as 15h da aula e pegou {transito} '
                              + 'min de trânsito')

                    casa.preparar_aula = False
                else:
                    print('A aula presencial só começa às 12h, e você só pode '
                          + 'se chegar a partir das 10h.')
            # Ir trabalhar[EAD]
            elif(opcao == 11):
                # O Salário é a diária por aula
                SALARIO = 200
                # A penalidade é acumulativa e desconta no salário.
                PENALIDADE = 0
                # Validando horário em que o personagem pode dar a aula
                if(17 <= relogio.horas < 22):

                    # Penalidade se o personagem está muito estressado
                    if(personagem.estressado >= 70):
                        print('Você foi dar a aula muito estressado,' +
                              'e acabou xingando o diretor! Por isso, ' +
                              'recebeu uma multa de 20% de redução do salário.'
                              )
                        PENALIDADE += 20/100
                    # Penalidade se o personagem está sujo
                    if(personagem.sujo):
                        print('Você foi dar a aula fedendo a cecê! Isso ' +
                              'incomodou bastante, e você foi penalizado com '
                              + 'de 10% do salário.'
                              )
                        PENALIDADE += 10/100

                    # Penalidade se o personagem está com fome
                    if(personagem.fome):
                        print('Você foi dar a aula com fome, e seu rendimento '
                              + 'abaixo do esperado! Você foi penalizado com '
                              + 'de 10% do salário.'
                              )
                        PENALIDADE += 10/100
                    # Penalidade se o personagem não preparou a aula
                    if(not(casa.preparar_aula)):
                        print('Você não preparou a aula, nesse caso seu ' +
                              'rendimento não foi satisfatório, por isso ' +
                              'sofrerá uma penalidade de redução de 30% ' +
                              'do salário')
                        PENALIDADE += 30/100
                    # Descontando as penalidades no salário
                    SALARIO += -SALARIO*PENALIDADE

                    # Verificando se o personagem está atrasado
                    if(19 <= relogio.horas < 22):
                        atraso_horas = relogio.horas-19
                        atraso_minutos = relogio.minutos
                        salario_atraso = round((
                            180-(atraso_horas*60 + atraso_minutos)
                        ) * SALARIO/180, 2)
                        print(f'Você está atrasado em {atraso_horas}h e ' +
                              f'{atraso_minutos} min.')
                        print('A cada aula(3h trabalhadas) você recebe R$200, '
                              + 'descontando todas as penalidades você recebeu'
                              + f' {salario_atraso}')
                        horario_saida = 180-(atraso_horas*60 + atraso_minutos)

                        personagem.salario(salario_atraso)
                        personagem.estresse(70)
                        relogio.avancaTempo(horario_saida)
                        print('Você saiu as 22h da aula EAD.')

                    else:
                        print('Você chegou no horário certo, vamos trabalhar!')
                        print(f'Você ganhou R${SALARIO} reais!')
                        personagem.salario(SALARIO)
                        personagem.estresse(35)
                        transito = aleatorios_multiplos_5(35, 120)
                        hora_saida = 21 - relogio.horas
                        minutos_saida = 60 - relogio.minutos
                        horario_saida = 60*hora_saida + minutos_saida

                        relogio.avancaTempo(horario_saida)
                else:
                    print('A aula EAD só começa às 19h, e você só pode ' +
                          'se conectar a partir das 17h.')

                casa.preparar_aula = False
            # Sair do jogo
            elif(opcao == 0):
                break

            # Quando for as 0h às 7h o personagem deve obrigatoriamente
            # estar dormindo!
            if(0 <= relogio.horas < 7):
                print('Seu personagem esta com sono, ' +
                      'aproveite para tirar uma boa noite de sono.')

                personagem.dormir()
                relogio.avancaTempo(7*60 - relogio.horas*60)
                relogio.dia += 1

            print('')
            print(personagem)
            print(relogio)
            print(casa)
        else:
            print('Opção inválida! Tente novamente.')

print('JOGO FINALIZADO!')
