#! python
def area(base, altura):
    area_terreno = base * altura
    print(f'A área do terreno retangular é: {area_terreno} u.a.')


base = float(input('Digite a base: '))
altura = float(input('Digite a altura: '))

area(base, altura)
