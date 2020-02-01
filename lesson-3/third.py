def my_func(first, second, third):
    args = (first, second, third)
    my_sum = sum(args)
    my_sum -= min(args)

    return my_sum


print(my_func(4, 9, 2))
