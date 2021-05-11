#! python
def calcula_salario(valor_hora, horas_trabalhadas):
    '''
        Essa função recebe os parâmetros valor_hora (o quanto vale a hora
        trabalhada do colaborador) e horas_trabalhadas (quantas horas o
        colaborador trabalhou). Ela retorna o valor do salário do colaborador,
        caso ele trabalhe mais de 40 horas, é acrescido um adicional de 1,5
        nas horas extras trabalhadas.
    '''
    if(horas_trabalhadas > 40):
        horas_extras = horas_trabalhadas - 40
        salario = valor_hora * (40 + 1.5 * horas_extras)
        return salario
    return valor_hora * horas_trabalhadas


valor_da_hora = float(input('Digite quanto o colaborador ganha por hora: '))
horas_de_trabalho = float(input('Digite o número de horas trabalhadas pelo '
                                + 'colaborador: '))

print(calcula_salario(valor_da_hora, horas_de_trabalho))
