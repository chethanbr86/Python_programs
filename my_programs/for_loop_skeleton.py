# 1st type:
# l1 = [[6,7,8],[66,77,88]]

# for i in l1:
#     for j in range(len(i)-1): #this is applicable to nested lists, throws error at single list
#         print(f'1:{i[j]}, 2:{i[j+1]}, 3:{j}, 4:{j+1}, 5:{i[j-1]}, 6:{j-1}')

# 2nd type: 
# l2 = [3,4,5]

# for i,j in enumerate(l2):
#     print(i,j)

# 3rd type:
l3 = [5,6,7]

for i in l3:
    for j in l3:
        print(i,j)
    