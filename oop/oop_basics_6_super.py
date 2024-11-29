#Super is a function used in child class to call methods from a parent class.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

class Circle(Shape):
    def __init__(self, color, radius, filled):
        super().__init__(color, filled)
        self.radius = radius

        
class Square(Shape):
    def __init__(self, color, width, filled):
        super().__init__(color, filled)
        self.width = width
    
class Triangle(Shape):
    def __init__(self, color, height, width, filled):
        super().__init__(color, filled)
        self.height = height
        self.width = width

#def init in every class has to be defined and it might lead to errors and hence creating a class called shape 
#which will have all the attributes and methods common to all the classes

circle = Circle("Red", 10, True)
print(circle.color)
print(circle.filled)
print(circle.radius)

square = Square("Blue", 20, True)
print(square.color)
print(square.filled)
print(square.width)

triangle = Triangle("Green", 30, 40, True)
print(triangle.color)
print(triangle.filled)
print(triangle.height)
print(triangle.width)