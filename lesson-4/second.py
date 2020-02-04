my_list = [3, 4, 6, 3, 6, 7, 2, 8, 34, 5, 6, 75, 3, 56, 2]

new_list = [my_list[element] for element in range(1, len(my_list)) if my_list[element] > my_list[element - 1]]

print(new_list)
