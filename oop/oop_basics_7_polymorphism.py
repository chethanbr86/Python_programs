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
    
# class Pizza:
#     def __init__(self, radius, topping):
#         self.radius = radius
#         self.topping = topping

#Pizza by itself will give error as it does not have area method, so changing the above code as below

class Pizza(Circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping

#Pizza now inherits from circle class and gives area

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza(8,'Pepperoni')]

for shape in shapes:
    print(shape.Area())