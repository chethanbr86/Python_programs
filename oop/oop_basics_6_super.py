#Super is a function used in child class to call methods from a parent class.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14 * 2 
    
class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def volume(self):
        return self.area() * self.height
    
class Square(Circle):
    def area(self):
        return self.radius * self.radius    
    
class Triangle(Circle):
    def area(self):
        return self.radius * self.radius * 2