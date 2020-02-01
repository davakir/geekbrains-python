"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    if not isinstance(word, str):
        raise ValueError

    return word.capitalize()


input_sentence = input('Введите предложение: ').split(' ')
for key, word in enumerate(input_sentence):
    input_sentence[key] = int_func(word)
sentence = ' '
sentence = sentence.join(input_sentence, )
print(sentence)
