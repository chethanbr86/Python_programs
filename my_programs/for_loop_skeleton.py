# 1st type:
# list_a = [[1,2],[1,2,3],[1,100,10]]

# for i in list_a:
#     for j in range(len(i)-1): #this is applicable to nested lists, throws error at single list, also range(len(i)-1) refers to index
#         print(f'1:{i[j]}, 2:{i[j+1]}, 3:{j}, 4:{j+1}, 5:{i[j-1]}, 6:{j-1}')

# 2nd type: 
# l2 = [3,4,5]

# for i,j in enumerate(l2):
#     print(i,j)

# 3rd type:
# l3 = [5,6,7]

# for i in l3:
#     for j in l3:
#         print(i,j)

# IMP: Making nested list into separate lists
# for i in range(len(list_a)):
#     sub_list = list_a[i]
#     print(sub_list)    

#checking reverse index in for loop
list_a = 'faghklmaddiddedd'
list_b = [11,22,43,41,25]
v = ['a','e','i','o','u']

# for i in range(len(list_b)):
#     for j in range(i-2,-1,-1):
#         print(f'i:{i}, value_at_i: {list_b[i]}, j:{j}, value_at_j: {list_b[j]}')

#Same like above with same solution (only for i), see the difference in code 
# for i in range(len(list_b)):
#     for j in range(i-1,0,-1):
#         print(f'i:{i}, value_at_i: {list_b[i]}, j:{j}, value_at_j: {list_b[j]}')

# my_list = [11,12,13,14,15,16,17]
# for i in range(len(my_list)-1, -1, -1):
#     print(i, my_list[i])

#sum of sub-array - not sure if its right
# def sum_array(list_b, i, j):
#     total = 0
#     for k in range(i, j+1):
#         total = total + list_b[i]
#     return total

# print(sum_array(list_b, 2, 5))

#Difference between adjacent elements
# diff_list = []
# def prefix_sum(list_b):
#     for i in range(1,len(list_b)):
#         diff_list.append(list_b[i] - list_b[i-1])
#     return diff_list

# print(prefix_sum(list_b))

# for i in range(0,len(list_a)-len(list_a)+3):
for i in list_a[:4]:
    if i in v:  
        print('yes',list_a[:4])
    else:
        print('no')

# print(range(0,len(list_a)-len(list_a)+3))
