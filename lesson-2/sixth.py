def is_string_empty(string):
    return not bool(len(string))

titles = ("название", "цена", "количество", "единицы")

goods = []
goods_count = 0
while True:
    print('Введите информацию о товаре')

    if not int(input('Есть информация по товарам? 1 = да, 0 = нет:  ')):
        break

    name = input('Наименование товара: ')
    if is_string_empty(name):
        print('Нужно ввести наименование. Давайте заново')
        continue

    price = input('Цена товара: ')
    if is_string_empty(price):
        print('Нужно ввести цену. Давайте заново')
        continue
    price = float(price)

    amount = input('Количество товара: ')
    if is_string_empty(amount):
        print('Нужно ввести количество, пусть даже 0. Давайте заново')
        continue
    amount = int(amount)

    goods_unit = input('Единица измерения товара: ')
    if is_string_empty(goods_unit):
        print('Нужно ввести единицу измерения. Давайте заново')
        continue

    goods_count = goods_count + 1

    good_info = {
        titles[0]: name,
        titles[1]: price,
        titles[2]: amount,
        titles[3]: goods_unit
    }

    goods.append((goods_count, good_info))

    print('Товары:')
    print(goods)

values = []
for good in goods:
    good = good[1]
    for number, title in enumerate(titles):
        values[number]
