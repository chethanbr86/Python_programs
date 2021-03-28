my_list = [5 ,4, 2, 1, 4 ,5]

new_list = []
for i in range(len(my_list)):
    if my_list[0] >= my_list[-1]:        
        new_list.append(my_list[0])
        my_list.pop(0)
    else:        
        new_list.append(my_list[-1])
        my_list.pop(-1)

print(new_list)

#Checking if its in descending order
flag = True
for j in range(len(new_list)):
    if new_list[0] < new_list[1]:
        flag = False
        break

if flag==True:
    print('Stacked correctly')
else:
    print('Not stacked correctly')


