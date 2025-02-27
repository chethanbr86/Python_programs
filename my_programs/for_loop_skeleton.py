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
list_b = [1,2,3,4,5,6,7,8]

for i in range(len(list_b)):
    for j in range(i-2,-1,-1):
        print(f'i:{i}, j:{j}')

