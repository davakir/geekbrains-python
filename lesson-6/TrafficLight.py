from itertools import cycle
from time import sleep


class TrafficLight:
    RED_COLOR = 'red'
    YELLOW_COLOR = 'yellow'
    GREEN_COLOR = 'green'

    __colors = ()
    __correct_colors_mode = (RED_COLOR, YELLOW_COLOR, GREEN_COLOR)

    def set_colors_mode(self, colors_mode):
        for key, info in enumerate(colors_mode):
            if info[0] != self.__correct_colors_mode[key]:
                raise RuntimeError('Нарушен порядок следования сигналов')

        self.__colors = colors_mode

    def running(self):
        for color, time in cycle(self.__colors):
            print(f'{color} signal lasts {time} seconds')
            sleep(time)


light = TrafficLight()
light.set_colors_mode((
    (TrafficLight.RED_COLOR, 3),
    (TrafficLight.YELLOW_COLOR, 5),
    (TrafficLight.GREEN_COLOR, 4)
))
light.running()