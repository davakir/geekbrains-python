"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def sum_init():
    total = 0

    def sum_numbers(numbers):
        nonlocal total
        for num in numbers:
            num = int(num)
            total += num

        return total

    return sum_numbers


def run(sum_function):
    end = False

    input_str = input('Введите строку чисел, разделенных пробелами: ')
    input_str = input_str.strip()
    numbers = tuple(input_str.split(' '))
    if 'Q' in numbers:
        index = numbers.index('Q')
        numbers = numbers[:index]
        end = True

    total = sum_function(numbers)

    if not end:
        print(f'Сумма всех чисел: {total}')
        return run(sum_function)

    return total


print('Вам нужно ввести строку чисел, разделенных пробелами. '
      'Окончанием работы программы считается введенный символ Q')

sum_func = sum_init()
result = run(sum_func)

print(f'Итоговая сумма: {result}')
