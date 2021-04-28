my_list = ['a','b','c','d','e']

index = 0
for i in my_list:    
    print(f'{i} index at: {index}')
    index = index + 1    

#with enumarate
for j in enumerate(my_list):
    print(j)

#But since we get solution in tuple, we can do tuple unpacking
for index, item in enumerate(my_list):
    print(f'{item} is at index: {index}')