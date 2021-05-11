#! python
def imprime_menor(primeiro, segundo):
    '''
        Essa função recebe 2 parâmetros genéricos(números, strings ou
        booleanos) e retorna o menor entre eles.
    '''

    if(primeiro < segundo):
        menor = primeiro
    else:
        menor = segundo
    print(f'O menor entre {primeiro} e {segundo} é {menor}')

# Não botarei nenhum input, pois vai atrapalhar na generalização da função
# (números, strings ou booleanos)


imprime_menor(True, False)
