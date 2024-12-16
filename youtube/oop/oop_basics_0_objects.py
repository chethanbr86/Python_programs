class Car:
    total_cars = 0
    def __init__(self, model, year, color, for_sale): 
        self.model = model    
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Car.total_cars += 1

    def __str__(self):
        return f"Model: {self.model}, Year: {self.year}, Color: {self.color}, For Sale: {self.for_sale}"
    
    @classmethod #This method does not use any attributes from __init__ and uses only class variable like total_cars
    def display_info(cls):
        return f"Total number of cars: {cls.total_cars}"
    
    def get_details(self, some_car):
        return f"Model: {self.model}, Year: {self.year}, Color: {self.color}, For Sale: {self.for_sale}, and this is {some_car}, total cars: {Car.total_cars}"

car1 = Car("Toyota", 2020, "Red", True)
car2 = Car("Honda", 2019, "Blue", False)

#without __str__
print(car1.model)
print(car2.year)
print(car1.color)
print(car2.for_sale)

#with __str__
print(car1)
print(car2)

#with classmethod
print(Car.display_info()) #But this does not display any attribute from __init__

#without classmethod
print(car1.get_details(car1.model)) #Also using placeholder with some_car
print(car2.get_details(car2.model))
