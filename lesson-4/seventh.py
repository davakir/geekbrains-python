"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
"""
from functools import reduce

def fibonachi_list():
    for number in range(1,16):
        yield reduce(lambda n, m: n * m, range(1, number+1))


for number in fibonachi_list():
    print(number)
