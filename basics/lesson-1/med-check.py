def age_title(age):
    age_last_unit = age % 10
    if 11 <= age <= 14 or age_last_unit == 0 or 5 <= age_last_unit <= 9:
        title = 'лет'
    elif age_last_unit == 1:
        title = 'год'
    else:
        title = 'года'
    return title

def print_contidion(fullname, age, weight, state):
    if state == 'good':
        state = 'хорошее состояние'
    elif state == 'passably':
        state = 'стоит заняться собой'
    else:
        state = 'следует обратиться ко врачу!'

    print(f'{fullname}, {age} {age_title(age)}, вес {weight} - {state}')


name = input('Input your name: ')
surname = input('Input your surname: ')
age = int(input('Input your age: '))
weight = float(input('Input your weight: '))

if age <= 30 and 50 < weight < 120:
    print(f'')

