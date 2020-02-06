from sys import argv


def count_salary(hours, salary_per_hour, bonus):
    return hours * salary_per_hour + bonus


try:
    script_name, hours, salary_per_hour, bonus = argv
    print(count_salary(int(hours), int(salary_per_hour), int(bonus)))
except ValueError:
    print('Not enough correct arguments')
