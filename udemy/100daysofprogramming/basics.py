# 2 types of function (input and output)
def add(n1, n2):
    print(n1 + n2)
add(2, 3)

def add(n1, n2):
    return n1 + n2
result = add(2, 3)
print(result)

list1 = [1, 2, 3]
list2 = [9, 8, 7]
new_list = list1 + list2
print(new_list)
list1 += list2
print(list1)
print(new_list)

# def a_function(a_parameter):    
#     a_variable = 15    
#     return a_parameter 
# a_function(10)
# print(a_variable)

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b) 
result = outer_function(5, 10)
print(result)

def foo(a, b=4, c=6):
    print(a, b, c) 
foo(20, c=12)

def all_aboard(a, *args, **kw): 
    print(a, args, kw) 
all_aboard(4, 7, 3, 0, x=10, y=64)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)

print('hello world \n hello world!')

import random
ran_int = random.randint(1,6)
ran = random.random()
print(ran_int,ran)


#String to list of strings
string1="This is Python" 
print("The actual string:",string1) 
#converting string1 into a list of strings
string2=string1.split()
print("The split string:",string2)
#applying list method to the individual elements of the list string1
list1=list(map(list,string2)) 
#printing the resultant list of lists
print("Converted to list of character list :\n",list1)
#printing to indivisual list of characters
list2 = list(string1)
print(list2)

#string with integers sepated by spaces
string1="1 2 3 4 5 6 7 8"
print("Actual String containing integers: ",string1)
print("Type of string: ",type(string1)) 
#coverting the string into list of strings
list1=list(string1.split())
print("Converted string to list : ",list1) 
#typecasting the individual elements of the string list into integer using the map() method
list2=list(map(int,list1))
print("List of integers : ",list2)