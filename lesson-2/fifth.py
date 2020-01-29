def is_string_digit(string):
    if len(string) != 0 and string.isdigit():
        return True
    else:
        return False


print('Давайте сформируем рейтинг. Сейчас рейтинг пуст, наполняем.')

raiting_list = []

# Формируем невозрастающую последовательность, например: 7 5 5 3 3 1
while True:
    number = input('Введите натуральное число, для остановки введите stop: ')

    if number == 'stop':
        break

    if not is_string_digit(number):
        print('Введено не число или не введено ничего, попробуйте еще раз')
        continue

    number = int(number)

    if len(raiting_list) == 0:
        raiting_list.append(number)
        print(raiting_list)
        continue

    for key, value in enumerate(raiting_list):
        if number >= raiting_list[key]:
            raiting_list.insert(key, number)
            break
        elif number < raiting_list[key]:
            if key == len(raiting_list) - 1:
                raiting_list.insert(key+1, number)
                break

    print(raiting_list)
