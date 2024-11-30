#Composition: Composition is a relationship between two classes where one class is dependant on another class. ("Owns-a relationship")

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horsepower, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_info(self):
        return f"Make: {self.make}, " + f"Model: {self.model}, " + f"Horsepower: {self.engine.horsepower}, " + f"Wheel Size: {self.wheels[0].size}"

car1 = Car("Toyota", "Camry", 200, 18)
car2 = Car("Honda", "Civic", 150, 17)

print(car1.display_info())
print(car2.display_info())
