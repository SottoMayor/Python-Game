from casa import Casa
from pessoa import Pessoa
from relogio import Relogio

from random import randint

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

    nome = input('Qual será o nome do seu personagem? ')

    personagem = Pessoa(nome)
    relogio = Relogio()
    casa = Casa()

    while True:
        print("=" * 100)
        print(personagem)
        print(relogio)
        print(casa)
        if(relogio.horas < 11):
            print('\nVocê tem que trabalhar às 12h, então saia de casa antes '
                  + 'das 11h. Não esqueca de preparar sua aula, antes de sair '
                  + 'de casa!\n')
        elif(11 <= relogio.horas < 12):
            print('Já passou das 11h, você poderá se atrasar! Saia agora para'
                  + ' ir trabalhar.')

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
        print("10 - Ir trabalhar")
        print("0 - Sair do jogo")
        opcao = int(input("Escolha sua ação: "))
        print("")
        if(0 <= opcao <= 10):
            if(opcao == 1):
                personagem.com_sujeira(False)
                relogio.avancaTempo(20)
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
            elif(opcao == 3):
                PRECO_ALIMENTO = 25
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

            elif(opcao == 4):
                lista_soneca = [num for num in range(1, 101) if num % 5 == 0]
                index_soneca = randint(0, len(lista_soneca) - 1)
                duracao_soneca = lista_soneca[index_soneca]
                print(f'Você tirou uma soneca de {duracao_soneca} minutos.')
                relogio.avancaTempo(duracao_soneca)
            elif(opcao == 5):
                pass
            elif(opcao == 6):
                lista_game = [num for num in range(30, 176) if num % 5 == 0]
                index_game = randint(0, len(lista_game) - 1)
                duracao_game = lista_game[index_game]
                print(f'Você passou {duracao_game} minutos jogando video ' +
                      'game.')
                relogio.avancaTempo(duracao_game)
            elif(opcao == 7):
                lista_celular = [num for num in range(1, 61) if num % 5 == 0]
                index_celular = randint(0, len(lista_celular) - 1)
                duracao_celular = lista_celular[index_celular]
                print(f'Você passou {duracao_celular} minutos mexendo no ' +
                      'celular.')
                relogio.avancaTempo(duracao_celular)
            elif(opcao == 8):
                pass
            elif(opcao == 9):
                pass
            elif(opcao == 10):
                pass
            elif(opcao == 11):
                pass
            elif(opcao == 0):
                break

            print('')
            print(personagem)
            print(relogio)
            print(casa)
        else:
            print('Opção inválida! Tente novamente.')

print('JOGO FINALIZADO!')
