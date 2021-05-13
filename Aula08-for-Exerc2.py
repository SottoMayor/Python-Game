#! python
nome = input('Digite seu nome: ')

control_a = control_e = control_i = control_o = control_u = 0

for letra in nome.lower():
    if(letra == 'a'):
        control_a += 1
    elif(letra == 'e'):
        control_e += 1
    elif(letra == 'i'):
        control_i += 1
    elif(letra == 'o'):
        control_o += 1
    elif(letra == 'u'):
        control_u += 1

print(f'a: {control_a}, e: {control_e}, i: {control_i}, o: {control_o}, '
      + f'u: {control_u}')
