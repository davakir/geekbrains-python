list1 = [3, 3, 4, 6, 6, 7, 9, 5, 5, 5, 0, 2]
list2 = [1, 2, 3, 4, 5]

for el1 in list1:
    if el1 in list2:
        list1.remove(el1)
        list2.remove(el1)

print(list1)


