import time
import itertools

class TrafficLight():
    def __init__(self):
        self.__color = [['red', 7], ['yellow', 2], ['green', 5]]

    def running(self):
        for color, sec in itertools.cycle(self.__color):
            print(color)
            time.sleep(sec)

tl_1 = TrafficLight()
tl_1.running()