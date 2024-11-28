class Animal:
    
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} eats')

    def sleep(self):
        print(f'{self.name} sleeps')

class Prey(Animal):
    def flee(self):
        print(f'{self.name} flees')

class Predator(Animal):
    def hunt(self):
        print(f'{self.name} hunts')    

class Rabbit(Prey):
    pass

class Fox(Predator):
    pass        

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Anna")
rabbit.flee()
rabbit.sleep()
rabbit.eat()

fox = Fox("Tim")
fox.hunt()
fox.sleep()
fox.eat()

fish = Fish("Bob")
fish.flee()
fish.hunt()
fish.sleep()
fish.eat()