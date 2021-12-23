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

