class Car:
    speed = 0
    color = ''
    name = ''

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed

    def go(self):
        print(f'Car {self.name} rides')

    def stop(self):
        print(f'Car {self.name} has been stopped')

    def turn(self, direction):
        print(f'Car {self.name} turned {direction}')

    def show_speed(self):
        print(f'Speed is {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = False

    def set_is_police(self, is_police):
        self.is_police = is_police


class SlowCar(Car):
    MAX_SPEED = 40

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print('Speed is exceeded')
        else:
            super().show_speed()


class TownCar(Car):
    MAX_SPEED = 60

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print('Speed is exceeded')
        else:
            super().show_speed()


police_car = PoliceCar('Police vehicle', 'blue', 110)
police_car.set_is_police(1)
police_car.go()
police_car.show_speed()
police_car.turn('left')
police_car.stop()

slow_car = SlowCar('VAZ-2101', 'orange', 30)
slow_car.go()
slow_car.show_speed()
