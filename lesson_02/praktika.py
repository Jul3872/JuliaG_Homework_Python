# Округление #

import math


def min_boxes(items):
    return math.ceil(items / 5)


num_items = int(input('Введите количество предметов - '))
print(f'Минимальное количество коробок - {min_boxes(num_items)}')
# из списка вывести второй и второй с конца элементы
# через запятую

employee_list = [
    "Jonh Snow",
    "Piter Pen",
    "Drakula",
    "IvanIV",
    "Moana",
    "Juilet"
    ]
print(employee_list[1] + ", " + employee_list[-2])


# создать функцию, которая принимает аргумент - число
# и возвращает Да, если оно делится на 3
# и Нет, если не делится
# вызвать функцию и передать в нее число
# результат сохранить в переменную


def dev_by_three(num):
    if num % 3 == 0:
        return 'Да'
    else:
        return 'Нет'


num = int(input('Введите число - '))
result = dev_by_three(num)

print(f'Делится ли на три {num}? - {result}')


"""модуль - Два делителя"""


def check_divisibility(n):
    for num in range(1, n+1):
        if num % 4 == 0:
            print(f'{num} - Делится на 2, и на 4')
        elif num % 2 == 0:
            print(f'{num} - Делится на 2, но не на 4')
        else:
            print(num)


check_divisibility(int(input('Введите число - ')))


# Квартал

def quarter_of_year(num_mon):
    if num_mon in {1, 2, 3}:
        return 'I квартал'
    elif num_mon in {4, 5, 6}:
        return 'II квартал'
    elif num_mon in {7, 8, 9}:
        return 'III квартал'
    elif num_mon in {10, 11, 12}:
        return 'IV квартал'
    else:
        return 'Неверные данные'


num_mon = int(input('Введите номер месяца - '))
print(quarter_of_year(num_mon))

# Фильтрация списка #

lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
result = [x for x in lst if x > 15 and x % 3 == 0]
print(result)

# Range #

spisok = list(range(25, 0, -5))
print(spisok)

# Поменять местами значения #

var_1 = 50
var_2 = 5

var_1, var_2 = var_2, var_1

print('var_1 = ', var_1)
print('var_2 = ', var_2)
