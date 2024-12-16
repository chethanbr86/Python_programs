class Prey:
    def flee(self):
        print('The prey flees')

class Predator:
    def hunt(self):
        print('The predator hunts')    

class Rabbit(Prey):
    pass

class Fox(Predator):
    pass        

class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
rabbit.flee()

fox = Fox()
fox.hunt()

fish = Fish()
fish.flee()
fish.hunt()