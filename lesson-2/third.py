winter = (12, 1, 2)
spring = (3, 4, 5)
summer = (6, 7, 8)
autumn = (9, 10, 11)

month = int(input('What month do you like? (input number) '))

if month in winter:
    print('You like winter!')
elif month in spring:
    print('You like spring!')
elif month in summer:
    print('You like summer!')
elif month in autumn:
    print('You like autumn!')