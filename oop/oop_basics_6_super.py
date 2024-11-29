#Super is a function used in child class to call methods from a parent class.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def Area(self):
        print(f'It is {self.color} and {'filled' if self.filled else 'not filled'}')    

class Circle(Shape):
    def __init__(self, color, radius, filled):
        super().__init__(color, filled)
        self.radius = radius

    def Area(self):
        super().Area() #This is done to bring the Area method from the parent class else it will give only the area method from the child class
        return f'Area of circle is {3.14 * self.radius * self.radius}'        
        
class Square(Shape):
    def __init__(self, color, width, filled):
        super().__init__(color, filled)
        self.width = width

    def Area(self):
        super().Area()
        return f'Area of square is {self.width * self.width}'
    
class Triangle(Shape):
    def __init__(self, color, height, width, filled):
        super().__init__(color, filled)
        self.height = height
        self.width = width

    def Area(self):
        super().Area()
        return f'Area of triangle is {0.5 * self.height * self.width}'

#def init in every class has to be defined and it might lead to errors and hence creating a class called shape 
#which will have all the attributes and methods common to all the classes

circle = Circle("Red", 10, True)
print(circle.color)
print(circle.filled)
print(circle.radius)
print(circle.Area())

square = Square("Blue", 20, True)
print(square.color)
print(square.filled)
print(square.width)
print(square.Area())

triangle = Triangle("Green", 30, 40, True)
print(triangle.color)
print(triangle.filled)
print(triangle.height)
print(triangle.width)
print(triangle.Area())