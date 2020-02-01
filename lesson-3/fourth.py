def negative_pow_v1(x, y):
    result = 1 / (x ** abs(y))
    return result


def negative_pow_v2(x, y):
    result = x
    for times in range(2, abs(y)+1):
        result *= x

    result = 1 / result
    return result


print(negative_pow_v1(2, -2))
print(negative_pow_v1(2, -3))
print(negative_pow_v2(2, -1))
print(negative_pow_v2(2, -5))

