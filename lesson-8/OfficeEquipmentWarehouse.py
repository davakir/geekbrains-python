class OfficeEquipment:
    type = 'base'

    def __init__(self, price, color, producer):
        self.price = price
        self.color = color
        self.producer = producer

    def get_params(self):
        return {
            'price': self.price,
            'color': self.color,
            'producer': self.producer
        }


class Printer(OfficeEquipment):
    type = 'printer'

    def set_multicolored(self, is_multicolored):
        self.multicolored = is_multicolored

    def get_params(self):
        params = super().get_params()
        params['is_multicolored'] = self.multicolored
        return params


class MoneyCounter(OfficeEquipment):
    type = 'money_counter'


class Computer(OfficeEquipment):
    type = 'computer'

    def set_weight(self, weight):
        self.weight = weight

    def get_params(self):
        params = super().get_params()
        params['weight'] = self.weight
        return params


class Warehouse:
    """
    Задание 6 предполагает, что где-то у параметров объектов выше должно быть указано их количество,
    но у одного объекта не может быть такого свойства,
    потому что и так предполагается работа с одним-единственным объектом.
    Максимум, что можно сделать, - это указывать, что для данного отдела оборудования достаточно.
    """

    equipment = {
        'Financial': {'max': 3, 'items': []},
        'IT': {'max': 5, 'items': []},
        'Administration': {'max': 2, 'items': []},
        'GarbageCollector': {'max': 99, 'items': []}
    }

    """
    Добавление оборудования происходит поединично.
    """
    def send_item_to_warehouse(self, item: OfficeEquipment):
        if item.type == 'computer':
            department = 'IT'
        elif item.type == 'money_counter':
            department = 'Financial'
        elif item.type == 'printer':
            department = 'Administration'
        else:
            department = 'GarbageCollector'

        check_result = self.check_equipment(department, item)
        if not check_result:
            raise OverflowError(f'Оборудование типа {item.type} для отдела {department} уже укомплектовано')

        self.equipment[department]['items'].append(item)

    def get_warehouse_items(self):
        return self.equipment

    def check_equipment(self, department, item: OfficeEquipment):
        if len(self.equipment[department]['items']) < self.equipment[department]['max']:
            return True
        else:
            return False


warehouse = Warehouse()
try:
    warehouse.send_item_to_warehouse(Printer(1000, 'white', 'Xerox'))
    warehouse.send_item_to_warehouse(Printer(3000, 'yellow', 'Brother'))
    warehouse.send_item_to_warehouse(Computer(15000, 'black', 'HP'))
    warehouse.send_item_to_warehouse(MoneyCounter(1000, 'white', 'Xerox'))
    warehouse.send_item_to_warehouse(OfficeEquipment(1000, 'white', 'KY'))
except Exception as err:
    print(err)

print(warehouse.get_warehouse_items())