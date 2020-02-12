"""
Employee больше подходит для сущности "сотрудник"
"""
class Employee:
    _income = {}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def set_income(self, salary, bonus):
        self._income = {'salary': salary, 'bonus': bonus}


"""
Должность никогда логически не может быть расширением сущности "сотрудник",
поэтому будем просто передавать извне сотрудника, у которого будем вызывать
указанные методы
"""
class EmployeePosition:
    def __init__(self, employee: Employee):
        self.__employee = employee

    def get_employee_full_name(self):
        return self.__employee.name + ' ' + self.__employee.surname

    def get_employee_total_income(self):
        return self.__employee._income['salary'] + self.__employee._income['bonus']


employee = Employee('Иван', 'Иванов', 'Монтажник')
employee.set_income(10000, 3000)
employee_position = EmployeePosition(employee)
print(employee_position.get_employee_full_name())
print(employee_position.get_employee_total_income())