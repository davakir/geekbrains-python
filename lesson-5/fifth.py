file_obj = open('files/tmp.txt', 'w')

numbers = input('Введите набор чисел, разделенных пробелами: ')

file_obj.write(numbers)

with open('files/tmp.txt') as file_obj:
    numbers = file_obj.readline().split()
    result = 0
    for number in numbers:
        if number.isdigit():
            result += int(number)

print(result)
