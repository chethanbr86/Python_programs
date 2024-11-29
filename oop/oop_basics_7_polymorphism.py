from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def Area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def Area(self):
        return self.width * self.width

class Triangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def Area(self):
        return 0.5 * self.height * self.width

shapes = [Circle(4), Square(5), Triangle(6,7)]

for shape in shapes:
    print(shape.Area())