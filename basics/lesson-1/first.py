# first
number = int(input('Input number: '))
print(number + 2)

# second
powed = False
while not powed:
    number = input('Input number between 0 and 10 excluding these ones: ')
    if  number[0] == '-':
        print('Your input is incorrect')
        continue
    else:
        number = int(number)

    if number == 0 or number > 9:
        print('Your input is incorrect')
        continue

    print(f'{number} to the power of 2 is {number**2}')
    powed = True
