#Class methods allow operations related to the class itself
#Class methods take cls as the first argument
#Static methods don't take self as the first argument as they don't need to access class data
#Instance methods take self as the first argument
#Self refers to the object or instance of the class but cls refers to the class itself

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa): #name and age are arguments and this whole funtion is called constructor
        self.name = name #instance variable
        self.gpa = gpa #self refers to the object currently working with
        Student.count += 1 #incrementing class variable
        Student.total_gpa += gpa

    def get_info(self): #instance method
        return f'{self.name} - {self.gpa}'
    
    @classmethod
    def get_count(cls): #class method
        return f'Total no. of students: {cls.count}'
    
    @classmethod
    def get_average_gpa(cls): #class method
        if cls.count == 0:
            return f'Average GPA: 0'
        return f'Average GPA: {cls.total_gpa/cls.count:.2f}'
    
student1 = Student("Michael", 4.5)
student2 = Student("Lincoln", 3.6)
student3 = Student("Sucre", 4.0)
student4 = Student("T-bag", 1.8)
    
print(student1.get_info()) #since get_info is not class method, we can't call by class name
print(Student.get_count())
print(Student.get_average_gpa())