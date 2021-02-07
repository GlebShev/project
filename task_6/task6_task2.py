class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def mass(self, layers):
        self._layers = layers
        mass = self._length * self._width * 25 * self._layers / 1000
        return mass

road = Road(100, 1000)
print(road.mass(10) , 'т')
