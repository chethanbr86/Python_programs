class Hunter: #class
    def __init__(self, Chethan, Nayana): #This init method with self belongs to the instance and not the class
        self.Chethan = Chethan
        self.Nayana = Nayana

#This is without init
# hunter1 = Hunter()  #instance1
# hunter2 = Hunter()  #instance2

#The below 4 lines were done before adding init 
# hunter1.Chethan = 11  #attribute1 and Chethan is attribute name or variable
# hunter2.Nayana = 23  #attribute2

# print(hunter1.Chethan)
# print(hunter2.Nayana)

#After defining init
hunter1 = Hunter(Chethan=11, Nayana=23)  #instance1
hunter2 = Hunter(86, 89)  #instance2

print(hunter1.Chethan, hunter2.Chethan, hunter1.Nayana, hunter2.Nayana)