#Static method belong to the class rather than the object (instance) of the class
#Instance method belongs to the object (instance) of the class
#Class method belongs to the class itself

#Difference between static method and class method is that static method can access class variables but class method cannot access class variables

class Employee:
    def __init__(self, name, position): #name and age are arguments and this whole funtion is called constructor
        self.name = name #instance variable
        self.position = position #self refers to the object currently working with 
        
    def get_details(self): #instance method
        return f'{self.name} = {self.position}'
    
    @staticmethod #static method
    def is_valid_position(position): #class method
        valid_positions = ['manager', 'developer', 'tester']
        return position in valid_positions
    
#To use static method name of class can be used rather than instance
print(Employee.is_valid_position('manager'))
print(Employee.is_valid_position('janitor'))

employee1 = Employee('John', 'manager')
employee2 = Employee('Jane', 'developer')
employee3 = Employee('Jim', 'tester')

#To call the instance method, we need to access one of the instances of the class
for employee in [employee1, employee2, employee3]:
    print(employee.get_details())