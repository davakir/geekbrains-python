def print_human_info(**info):
    """Выводит имя, фамилию, год рождения, город проживания, email, телефон"""
    output_str = ''

    for key, value in info.items():
        output_str += f'{key.capitalize()}: {value}. '

    print(output_str)


print_human_info(
    имя='Екатерина',
    фамилия='Арагонская',
    год_рождения=1485,
    город='Alcala',
    email='caterina@mail.ru',
    телефон=9998877
)
