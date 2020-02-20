class ZeroDivisionException(ZeroDivisionError):
    pass

try:
    try:
        10 / 0
    except ZeroDivisionError:
        raise ZeroDivisionException('Division by zero is not allowed')
except ZeroDivisionException as error:
    print(error)
    exit(1)
