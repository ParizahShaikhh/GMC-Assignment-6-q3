# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area().
# Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


r = Rectangle(10, 20)
print(f"Area of rectangle: {r.area()}")  # Output: Area of rectangle: 200

# Why Use Abstract Classes?
# To define a common interface for all subclasses
# To enforce that all subclasses implement specific behavior (like area())
# real-world system (like Animal or Employee)
