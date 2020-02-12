with open('files/salaries.txt') as file_obj:
    salaries_sum = 0
    employees_count = 0
    for employee in file_obj.readlines():
        employee = employee.split()
        salaries_sum += float(employee[1])
        employees_count += 1
        if float(employee[1]) < 20000:
            print(employee[0])

    average = salaries_sum / employees_count

    print(f'Average salary is {average:.2f}')
