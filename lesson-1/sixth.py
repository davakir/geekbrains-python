def is_string_digit(string):
    if len(string) != 0 and string.isdigit():
        return True
    else:
        return False

first_day_distance = input('Дистанция пробежки в первый день (км): ')
if not is_string_digit(first_day_distance):
    print('Введено не число или не введено ничего, выходим')
    exit(1)
first_day_distance = int(first_day_distance)

goal_distance = input('Цель пробежки - дистанция в км: ')
if not is_string_digit(goal_distance):
    print('Введено не число или не введено ничего, выходим')
    exit(1)
goal_distance = int(goal_distance)
if goal_distance < first_day_distance:
    print('Некорректная целевая дистанция, должна быть больше первого дня пробежки, выходим')
    exit(1)

goal_day = 1
distance = first_day_distance
while distance < goal_distance:
    distance *= 1.1
    goal_day += 1
    print("%d-й день: %.2f км" % (goal_day, distance))

print(f'На {goal_day}-й день спортсмен достиг результата — не менее {goal_distance} км')