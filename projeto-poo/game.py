# Fazer a nossa historinha, nesse arquivo!

from casa import Casa
from pessoa import Pessoa
from relogio import Relogio


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

    nome = input('Qual sera o nome do seu personagem? ')

    personagem = Pessoa(nome)
    relogio = Relogio()
    casa = Casa()

    while True:
        print("=" * 100)
        print('')
        print(personagem)
        print('')
        print(relogio)
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
        print("8 - Ir à academia")
        print("9 - Ir ao mercado")
        print("10 - Preparar a aula")
        print("11 - Ir trabalhar")
        print("0 - Sair do jogo")
        opcao = int(input("Escolha sua ação: "))
        break

print('JOGO FINALIZADO!')
