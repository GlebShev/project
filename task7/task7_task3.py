class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return f'Сложение: {self.count + other.count}'

    def __sub__(self, other):
        return f'Вычитание: {self.count - other.count}' if self.count > other.count else "Вычитание не может быть сделано"

    def __mul__(self, other):
        return f'Умножение: {self.count * other.count}'

    def __truediv__(self, other):
        return f'Деление: {self.count / other.count}'

    def make_order(self, quantity):
        num_1 = self.count // quantity
        num_2 = self.count % quantity
        return '\n'.join('*' * quantity for i in range(num_1)) + '\n' + '*' * num_2

cell_1 = Cell(30)
cell_2 = Cell(2)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(9))
