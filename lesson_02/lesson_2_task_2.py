def is_year_leap(year):
    if year % 4 == 0:
        return 'True'
    else:
        return 'False'


years = [2024, 2017]
for year in years:
    result = is_year_leap(year)
    print(f'год {year}: {result}')

# year_1 = 2024
# year_2 = 2017
#
# result_1 = is_year_leap(year_1)
# result_2 = is_year_leap(year_2)

# print(f"год {year_1}: {result_1}")
# print(f"год {year_2}: {result_2}")
