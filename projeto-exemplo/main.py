from relogio import Relogio
from personagem import Personagem
from casa import Casa

if(__name__ == "__main__"):  # Pesquisar significado desse if
    dia = 1
    relogio = Relogio()
    personagem = Personagem()
    casa = Casa()
    cafe_da_manha = False
    while True:
        print("---")
        print("São "+str(relogio)+" do dia "+str(dia) +
              ". Você tem que sair pro trabalho até às 07:00.")
        print(personagem)
        print("")
        print("Ações:")
        print("1 - Tomar banho e escovar os dentes")
        print("2 - Fazer café da manhã")
        print("3 - Pedir café da manhã")
        print("4 - Tomar café da manhã")
        print("5 - Tomar remédio")
        print("6 - Comprar remédio")
        print("7 - Ir trabalhar")
        print("0 - Sair do jogo")
        opcao = input("Escolha sua ação:")
        if(opcao == "1"):
            personagem.sujo = False
            relogio.avancaTempo(20)
        elif(opcao == "2"):
            if(casa.comida > 0):
                casa.comida -= 1
                cafe_da_manha = True
            else:
                print("Não há comida em casa.")
            relogio.avancaTempo(15)
        elif(opcao == "3"):
            if(personagem.dinheiro >= 15):
                personagem.dinheiro -= 15
                cafe_da_manha = True
            else:
                print(
                    "O café da manhã custa 15 reais, você não tem dinheiro " +
                    "suficiente.")
            relogio.avancaTempo(5)
        elif(opcao == "4"):
            if(cafe_da_manha):
                personagem.fome = False
                cafe_da_manha = False
                relogio.avancaTempo(15)
            else:
                print("Não tem café da manhã na sua casa.")
                relogio.avancaTempo(5)
        elif(opcao == "5"):
            if(casa.remedios > 0):
                casa.remedios -= 1
                personagem.medicado = True
            else:
                print("Não tem remédio na sua casa")
            relogio.avancaTempo(5)
        elif(opcao == "6"):
            if(personagem.dinheiro >= 20):
                casa.remedios += 10
                personagem.dinheiro -= 20
                relogio.avancaTempo(10)
            else:
                print(
                    "A cartela com 10 remédios custa 20 reais, você não tem " +
                    "dinheiro suficiente.")
                relogio.avancaTempo(5)
        elif(opcao == "7"):
            print("-=-=-")
            print("Você foi trabalhar.")
            print(personagem)
            print("-=-=-")
            recebido = personagem.salario
            if(not personagem.medicado):
                print(
                    "Como você não tomou seu remédio, você ficou doente no " +
                    "caminho e não chegou no trabalho")
                recebido = 0
            elif(personagem.sujo):
                print(
                    "Como você estava sujo, seus colegas reclamaram para seu" +
                    " chefe, e você levou uma advertência.")
                recebido *= 0.9
            elif(personagem.fome):
                print(
                    "Como você estava com fome, você trabalhou metade do que" +
                    " consegue trabalhar.")
                recebido *= 0.5
            elif(relogio.atrasado()):
                print(
                    "Como você chegou atrasado, você produziu menos do que" +
                    " de costume.")
                recebido *= 0.8
            print("Você recebeu "+str(recebido) +
                  " reais pelo seu trabalho hoje.")
            print("-=-=-")

            personagem.dinheiro += recebido
            personagem.dormir()
            relogio = Relogio()
            dia += 1
        elif(opcao == "0"):
            break
        else:
            print("Opção inválida!")
            relogio.avancaTempo(5)
