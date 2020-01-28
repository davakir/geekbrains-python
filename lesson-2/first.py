just_a_list = [3, 'Hello', 9.99, ['Lesson'], {'key': 'value'}, ('first', 'sec', 'third'), False]

for element in just_a_list:
    if isinstance(element, str):
        print(f'{element} is string!')
    elif isinstance(element, int):
        print(f'{element} is integer!')
    elif isinstance(element, float):
        print(f'{element} is float number!')
    elif isinstance(element, list):
        print(f'{element} is list')
    elif isinstance(element, dict):
        print(f'{element} is dictionary!')
    elif isinstance(element, tuple):
        print(f'{element} is tuple!')
    elif isinstance(element, bool):
        print(f'{element} is boolean!')

print("\n")

for element in just_a_list:
    if type(element) == str:
        print(f'{element} is string!')
    elif type(element) == int:
        print(f'{element} is integer!')
    elif type(element) == float:
        print(f'{element} is float number!')
    elif type(element) == list:
        print(f'{element} is list')
    elif type(element) == dict:
        print(f'{element} is dictionary!')
    elif type(element) == tuple:
        print(f'{element} is tuple!')
    elif type(element) == bool:
        print(f'{element} is boolean!')
