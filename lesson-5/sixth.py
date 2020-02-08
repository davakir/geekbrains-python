studying_dict = {}

EMPTY_SIGN = '-'

with open('files/studying_plan.txt') as file_obj:
    for line in file_obj.readlines():
        info = line.split()

        title = info.pop(0)
        count = 0
        try:
            for studying_type in info:
                if EMPTY_SIGN not in studying_type:
                    count += int(studying_type)
        except ValueError:
            print(f'Набор данных неверен для {title}, кол-во занятий должно быть натуральным числом')

        studying_dict[title] = count

print(studying_dict)
