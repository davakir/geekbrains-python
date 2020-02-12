class Road:
    ASPHALT_WEIGHT_PER_SQUARE_METER_IN_KILOS = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_asphalt_weight(self, thickness):
        return self._length * self._width * thickness * self.ASPHALT_WEIGHT_PER_SQUARE_METER_IN_KILOS


road = Road(30, 1000)
print(road.count_asphalt_weight(2), 'kilos')
