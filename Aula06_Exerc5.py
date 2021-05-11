#! python
def IMC(peso, altura):
    '''
        Essa função recebe o peso(kg) e a altura(m) e retorna o IMC
        do indivíduo.
    '''
    return round(peso / pow(altura, 2), 2)


print(IMC(75, 1.68))
