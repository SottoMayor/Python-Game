#! python
def soma_imposto(taxa_imposto, custo):
    '''
        Essa função recebe a taxa de imposto(%) paga no produto e o valor do
        produto, respectivamente. Ela retorna o valor total do produto,
        sendo o valor do produto mais a taxa de imposto.

    '''

    custo_atualizado = custo + taxa_imposto/100 * custo
    return custo_atualizado


preco = float(input('Digite o preco: '))
porcentagem_imposto = float(input('Digite a taxa de imposto(%): '))

print(soma_imposto(porcentagem_imposto, preco))
