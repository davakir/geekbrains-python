with open('files/first.txt', 'w+') as file_object:
    while True:
        string = input('Input something: ')
        if string:
            print(string, file=file_object)
        else:
            print('Input has been stopped')
            break
