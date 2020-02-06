"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка
"""
from functools import reduce


def multiplication(multiplier_1, multiplier_2):
    return multiplier_1 * multiplier_2


my_list = [number for number in range(100, 1001) if number % 2 == 0]
print(reduce(multiplication, my_list))
