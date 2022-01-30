# Swap first and last element of list
from re import X

#Method 1: 
# def swap(new_list):
#     x = new_list[0]
#     new_list[0] = new_list[-1]
#     new_list[-1] = x
#     return new_list

# inp = [12, 35, 9, 56, 24]
# print(swap(inp))

#Method 2:
# def swap(new_list):
#     new_list[0], new_list[-1] = new_list[-1], new_list[0]
#     return new_list

# inp = [12, 35, 9, 56, 24]
# print(swap(inp))

#Method 3:
# def swap(new_list):
#     start,*middle,end = new_list
#     new_list = [end, *middle, start]
#     return new_list

# inp = [12, 35, 9, 56, 24]
# print(swap(inp))

#Method 4:
def swap(new_list):
    first = new_list.pop(-1) #0
    last = new_list.pop(0) #-1

    new_list.insert(0, first) #last
    new_list.append(last) #first

    return new_list

inp = [12, 35, 9, 56, 24]
print(swap(inp))