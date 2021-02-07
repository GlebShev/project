from abc import ABC, abstractmethod

class Cothes(ABC):

    def __init__(self, param):
        self.param = param
    @abstractmethod
    def calc(self):
        pass

class Coat(Cothes):
    @property
    def calc(self):
        return round(self.param/6.5 + 0.5, 2)

class Suit(Cothes):
    @property
    def calc(self):
        return round(2 * self.param + 0.3, 1)

coat = Coat(5)
suit = Suit(5)

print(coat.calc)
print(suit.calc)