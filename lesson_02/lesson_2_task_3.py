import math


def square(a):
    return math.ceil(a * a)


a = float(input('Введите длину стороны квадрата - '))
result = square(a)
print(f'Площадь квадрата с округлением вверх: {result}')
