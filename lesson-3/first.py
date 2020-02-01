def division(divident, divider):
    try:
        result = divident / divider
        return result
    except ZeroDivisionError:
        print('На ноль делить нельзя, давайте заново')
        raise Exception


def run():
    try:
        divident = int(input('Введите делимое: '))
        divider = int(input('Введите делитель: '))

        print(division(divident, divider))
    except ValueError:
        print('Введено не число, давайте заново')
        run()
    except Exception:
        run()


run()
