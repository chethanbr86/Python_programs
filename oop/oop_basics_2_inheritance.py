class Animal:
    no_of_animals = 3
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_alive = True
        Animal.no_of_animals += 1

    def eat(self):
        print(f'{self.name, self.age} is eating')

    def sleep(self):
        print(f'{self.name, self.age} is sleeping')

    def run(self):
        print(f'{self.name, self.age} is running')

class Dog(Animal): #Dog class inheriting attributes and methods of parent class Animal
    def speak(self):
        print('Woof')

class Cat(Animal): #Cat class inheriting attributes and methods of parent class Animal
    no_of_cats = 5
    def total():
        Cat.no_of_cats += 1

cat1 = Cat('Furry', 4) #object
cat2 = Cat('Cherry', 5)

class Mouse(Animal): #Mouse class inheriting attributes and methods of parent class Animal
    pass

dog = Dog("Scooby", 3)
cat = Cat("Tom", 2)
mouse = Mouse("Jerry", 1)

#Even though dog cat and mouse classes are empty, they are inheriting from animal class
print(dog.name)
print(cat.is_alive)
print(mouse.age)
mouse.eat()
dog.sleep()
cat.run()

#If dog has its own method and cat has its own class variable
dog.speak()
print(Cat.no_of_cats) #should have been 7 but showing 5
print(Animal.no_of_animals) #But this is shown correctly