def is_string_digit(string):
    if len(string) != 0 and string.isdigit():
        return True
    else:
        return False

proceeds = input('Введите объем выручки фирмы: ')
if not is_string_digit(proceeds):
    print('Введено не число или не введено ничего, выходим')
    exit(1)
proceeds = int(proceeds)
if not proceeds:
    print('Работали очень плохо, выручка нулевая')
    exit(0)

costs = input('Введите объем издержек фирмы: ')
if not is_string_digit(costs):
    print('Введено не число или не введено ничего, выходим')
    exit(1)
costs = int(costs)

profit = proceeds - costs
if profit:
    print(f'Прибыль фирмы составляет {profit} у.е.')
else:
    print(f'Убыток фирмы составляет {profit} у.е.')
    exit()

employees_number = input('Введите количество сотрудников фирмы: ')
if not is_string_digit(employees_number):
    print('Введено не число или не введено ничего, выходим')
    exit(1)
employees_number = int(employees_number)
if not employees_number:
    print('Неплохо работает фирма без сотрудников!')
    exit()

profit_per_employee = profit // employees_number
print(f'Прибыль в пересчете на каждого сотрудника составляет {profit_per_employee}')