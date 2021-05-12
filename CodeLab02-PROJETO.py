#! python
def custo_hotel(dias):
    return dias * 140.00 if dias > 0 else 'Entrada inválida'


def custo_aviao(cidade):

    cidade = cidade.upper()

    if(cidade == 'SÃO PAULO'):
        return 312.00
    elif(cidade == 'PORTO ALEGRE'):
        return 477.00
    elif(cidade == 'RECIFE'):
        return 831.00
    elif(cidade == 'MANAUS'):
        return 986.00
    else:
        return 'Entrada de cidade inválida!'


def custo_carro(dias):
    custo = dias * 40.00

    if(0 <= dias < 3):
        custo = custo
    elif(3 <= dias < 7):
        custo = custo - 20
    elif(dias >= 7):
        custo = custo - 50
    else:
        return 'A entrada DIAS foi digitada de forma incorreta!'

    return custo


def gastos_extras(gastos):
    return gastos if gastos >= 0 else 'Entrada inválida!'


def calculo_total(cidade, dias, gastos):

    soma_de_gastos = custo_hotel(
        dias) + custo_aviao(cidade) + custo_carro(dias) + gastos_extras(gastos)

    print(f'O custo com hotel foi R${custo_hotel(dias)}, o custo com passagens'
          + f' foi R${custo_aviao(cidade)} e o custo com carro foi de'
          + f' R${custo_carro(dias)}, além disso seus gastos extras foram de'
          + f' {gastos_extras(gastos)}. Portanto o gasto total foi de'
          + f' R${soma_de_gastos}')


calculo_total('Manaus', 12, 800)
