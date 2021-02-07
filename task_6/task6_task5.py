class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Ручка рисует')

class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует')

class Handle(Stationery):
    def draw(self):
        print('Маркер рисует')

pen = Pen('ручка')
handle = Handle('Маркер')
brush = Stationery('Кисточка')

pen.draw()
handle.draw()
brush.draw()

