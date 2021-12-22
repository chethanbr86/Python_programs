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