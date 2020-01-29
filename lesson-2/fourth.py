string = input('Введите строку из нескольких слов: ')

string = string.split(' ')

for num, word in enumerate(string):
    if len(word) > 10:
        word = word[:10]

    print(f'{num+1}: {word}')
