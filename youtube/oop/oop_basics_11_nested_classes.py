# class Employee:
#     print('Employee class 1')

#     class Employee:
#         print('Employee class 2')

# class Employee:
#     print('Employee class 3')

#Like seen above two classes can have same name which leads to conflict and hence nested classes can be used
#Above one will not be a problem if they are within different classes like shown below

# class Company1:
#     class Employee:
#         print('Employee class 1')

# class Company2:
#     class Employee:
#         print('Employee class 2')     

#The above code will not create conflict

class Company:
    #Try adding company names in output with employee of corresponding company
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            print(f'{self.name} - {self.position}')

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees] #For this method, use like called below
    
    # def list_employees(self):
    #     return [f"{employee.name} - {employee.position}" for employee in self.employees] #For this method, use like called below

company1 = Company('Google')
company2 = Company('Microsoft')

company1.add_employee('John', 'Manager')
company1.add_employee('Jane', 'Developer')
company1.add_employee('Jim', 'Tester')

company2.add_employee('Jack', 'CEO')
company2.add_employee('Jill', 'Vice President')

company1.list_employees()
company2.list_employees()

# for employee in company1.list_employees():
#     print(employee)
