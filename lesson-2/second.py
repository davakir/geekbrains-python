print('Заполняем список')

end_marker = 'end'
just_a_list = []
while True:
    element = input('Введите элемент для добавления в список, если хотите закончить, введите \'end\': ')
    if element != end_marker:
        just_a_list.append(element)
    else:
        print('Закончили заполнять список')
        break

print(just_a_list)

just_a_list_length = len(just_a_list)

if just_a_list_length % 2 == 0:
    has_even_elements_count = True
else:
    has_even_elements_count = False

start = 0
step = 2
while start < just_a_list_length:
    if has_even_elements_count or start != just_a_list_length - 1:
        length = 2
    else:
        break

    elements = just_a_list[start:start+length]

    just_a_list[start] = elements[1]
    just_a_list[start + 1] = elements[0]

    start += step

print(just_a_list)
