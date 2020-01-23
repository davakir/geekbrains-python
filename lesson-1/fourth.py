def is_string_digit(string):
    if len(string) != 0 and string.isdigit():
        return True
    else:
        return False

digit_in_string_format = input('Введите положительное число: ')

if is_string_digit(digit_in_string_format) == False:
    print('Введено не число или не введено ничего, выходим')
    exit(1)

splitted_digit = list(digit_in_string_format)

max_numeral = splitted_digit[0]
for symbol in splitted_digit:
    if max_numeral < symbol:
        max_numeral = symbol

print(f'Максимальная цифра в числе: {max_numeral}')