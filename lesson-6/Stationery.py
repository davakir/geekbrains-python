class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Start drawing...')


class Pen(Stationery):
    def draw(self):
        print(f'{self._title} starts drawing...')

class BilliardMarker(Stationery):
    def draw(self):
        print(f'{self._title} starts drawing with thick line...')

class Pencil(Stationery):
    def draw(self):
        print(f'{self._title} starts drawing with gray line...')

b_marker = BilliardMarker('Жирный маркер')
b_marker.draw()

pencil = Pencil('Простой карандаш')
pencil.draw()