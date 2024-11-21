class Student:

    class_year = 2024 #class variable
    num_students = 0 #class variable

    def __init__(self, name, age): #name and age are arguments and this whole funtion is called constructor
        self.name = name #instance variable
        self.age = age #self refers to the object currently working with
        Student.num_students += 1 #incrementing class variable #If we are modifying class variable then use class name in place of self as shown

    def room(self, no_room): #This function is called method
        self.no_room = 5

student1 = Student("Michael", 30) #object
student2 = Student("Lincoln", 32)
student3 = Student("Sucre", 28)
student4 = Student("T-bag", 40)

print(f'Graduating class of prison break {Student.class_year} has {Student.num_students} students')
print(student1.name)

print(student1.class_year)  #accessing from instance variable
#or 
print(Student.class_year)  #accessing from class name