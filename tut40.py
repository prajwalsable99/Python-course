#Abstract class
from abc import ABC,abstractmethod


class shape(ABC):
    @abstractmethod
    def Area(self):
        return 0

class Rectangle(shape):
    poly="quadrilateral"
    sides=4
    def __init__(self):
        self.length=8
        self.width=6
    def Area(self):
        return self.length*self.width


rect1 =Rectangle()
print(rect1.Area())