"""
    Abstract classes are classes that contain one or more abstract methods.
    An abstract method is a method that has a declaration but does not have an implementation.
    Abstract classes cannot be instantiated on its own (i.e; prevents instantiation of class itself) but rather to be subclassed by other classes.
    Abstract classes are useful when you want to define a common interface for a set of subclasses.
"""

from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass     

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle started")

    def stop(self):
        print("Motorcycle stopped")

car = Car()
car.start()
car.stop()

motorcycle = Motorcycle()
motorcycle.start()
motorcycle.stop()
