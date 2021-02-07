class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')

    def show_speed(self):
        print(f'Скорость сейчас: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Скорость больше нормы!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Скорость больше нормы!')

class PoliceCar(Car):
    pass

town_car = TownCar(70, 'green', 'smart', False)
sport_car = SportCar(110, 'blue', 'ferrari', False)

town_car.show_speed()
town_car.go()
town_car.stop()
town_car.turn('Right')

sport_car.show_speed()
sport_car.go()
sport_car.stop()
sport_car.turn('Left')




