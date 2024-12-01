#Check if the input is Armstrong number
num = 153

#converting input into a list 
print(type(num))
num_list = list(map(int,str(num)))

#Cubing each number
cube_list = list(map(lambda x:x**3, num_list))
print(cube_list)

""" total=0
for i in cube_list:
    total += i """

if num == sum(cube_list):
    print('Armstrong number')
else:
    print('Not an Armstrong number')







