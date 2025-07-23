def month_to_season(num_mon):
    if num_mon in {12, 1, 2}:
        return ('Зима')
    elif num_mon in {3, 4, 5}:
        return ('Весна')
    elif num_mon in {6, 7, 8}:
        return ('Лето')
    elif num_mon in {9, 10, 11}:
        return ('Осень')
    else:
        return ('Введены некорректные данные')


num_mon = int(input('Введите номер месяца в диапазоне от 1 до 12 - '))
print(month_to_season(num_mon))
