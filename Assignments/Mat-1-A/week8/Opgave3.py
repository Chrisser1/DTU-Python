from abc import abstractmethod
from math import pi


class Shape():
    @abstractmethod
    def get_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.__radius = radius

    def get_area(self) -> float:
        return pi * self.__radius**2


class Square(Shape):
    def __init__(self, side_length: float):
        super().__init__()
        self.__side_length = side_length

    def get_area(self):
        return self.__side_length * self.__side_length


if __name__ == "__main__":
    square = Square(10)
    circle = Circle(10)

    print(f"square area = {square.get_area()} and circle area = {circle.get_area()}")
