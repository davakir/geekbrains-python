def generator_read_file_lines(file_to_read_object):
    while True:
        line = file_to_read_object.readline()
        if not line:
            break
        yield line


file_name = 'files/second.txt'

with open(file_name, 'w') as file_object:
    while True:
        string = input('Input something: ')
        if string:
            print(string, file=file_object)
        else:
            break

with open(file_name) as file_to_read:
    lines_count = 0
    for line in generator_read_file_lines(file_to_read):
        print(f'В {lines_count+1} строке {len(line.split())} слов')
        lines_count += 1
    print(f'Всего в файле {lines_count} строк')
