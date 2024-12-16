#Trying with codeium

#OOP concepts
#1. Inheritance
#2. Polymorphism
#3. Encapsulation
#4. Abstraction
#5. Data Hiding

#1. Inheritance example

class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def eat(self):
        print(f'{self.name} is eating') 

animal = Animal('Dog')
animal.eat()
print(animal.name) #without __str__
print(animal) #with __str__

#4. Abstraction example

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius * self.radius
    
circle = Circle(10)
print(circle.Area())