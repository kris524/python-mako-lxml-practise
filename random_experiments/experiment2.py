from typing import Protocol
import math

# In this exercise, you'll
# implement two classes representing geometric
# shapes, a Circle and a Rectangle, that both conform to a
#  Shape protocol. You'll also create a function that
# accepts any object conforming to the Shape protocol
#  and calculates its perimeter.


class Shape(Protocol):
    def area(self) -> float:
        pass

    def perimiter(self) -> float:
        pass


class Rectangle:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def area(self) -> float:
        return self.a * self.b

    def perimiter(self) -> float:
        return 2 * (self.a + self.b)


class Circle:
    def __init__(self, a: float):
        self.a = a

    def area(self) -> int:
        return (self.a**2) * math.pi

    def perimiter(self) -> float:
        return 2 * math.pi * self.a


def calculate_area(shape: Shape) -> float:
    return shape.area()


def calculate_peremiter(shape: Shape) -> float:
    return shape.perimiter()


if __name__ == "__main__":
    cir = Circle(2)
    print(calculate_area(cir))

    rec = Rectangle(1, 2)
    print(calculate_peremiter(rec))
