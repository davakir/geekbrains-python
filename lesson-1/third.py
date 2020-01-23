def is_string_digit(string):
    if len(string) != 0 and string.isdigit():
        return True
    else:
        return False

def enlarge_list_of_symbols(listed_symbols, times):
    result = []
    while times > 0:
        result = result + listed_symbols
        times -= 1

    return result

def sum_list_of_digits(list_of_digits):
    result = 0
    for digit in list_of_digits:
        result += int(digit)

    return result

digit_in_string_format = input('Введите положительное число: ')

if not is_string_digit(digit_in_string_format):
    print('Введено не число или не введено ничего, выходим')
    exit(1)

digit_divided_char_by_char = list(digit_in_string_format)

single = sum_list_of_digits(digit_divided_char_by_char)
doubled = sum_list_of_digits(enlarge_list_of_symbols(digit_divided_char_by_char, 2))
tripled = sum_list_of_digits(enlarge_list_of_symbols(digit_divided_char_by_char, 3))

result = single + doubled + tripled
print(f'Итоговая сумма введенного числа n + посимвольно удвоенного nn + посимвольно утроенного nnn: {result}')


