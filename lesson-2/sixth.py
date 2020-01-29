def is_string_empty(string):
    return not bool(len(string))

titles = ("название", "цена", "количество", "единицы")

goods = []
goods_count = 0
while True:
    print('Введите информацию о товаре')

    if not int(input('Есть информация по товарам? 1 = да, 0 = нет:  ')):
        break

    good_info = {}

    name = input('Наименование товара: ')
    if is_string_empty(name):
        print('Нужно ввести наименование. Давайте заново')
        continue
    good_info[titles[0]] = name

    price = input('Цена товара: ')
    if is_string_empty(price):
        print('Нужно ввести цену. Давайте заново')
        continue
    price = float(price)
    good_info[titles[1]] = price

    amount = input('Количество товара: ')
    if is_string_empty(amount):
        print('Нужно ввести количество, пусть даже 0. Давайте заново')
        continue
    amount = int(amount)
    good_info[titles[2]] = amount

    goods_unit = input('Единица измерения товара: ')
    if is_string_empty(goods_unit):
        print('Нужно ввести единицу измерения. Давайте заново')
        continue
    good_info[titles[3]] = goods_unit

    goods_count = goods_count + 1

    goods.append((goods_count, good_info))

    print('Товары:')
    print(goods)

statistics = {}
for title in titles:
    items = []
    for good in goods:
        good_info = good[1]
        if not good_info[title] in items:
            items.append(good_info[title])

    statistics[title] = items

print(statistics)