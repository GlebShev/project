class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

class Position(Worker):
    def get_full_name(self):
        name = f'{self.name} {self.surname}'
        return name

    def get_total_income(self):
        salary = self._income_wage +  self._income_bonus
        return salary

worker = Position('Anton', 'Rybakov', 'boss', {'wage': 100, 'bonus': 10})
print(worker.get_full_name())
print(worker.get_total_income())