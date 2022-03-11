#Print hightest number in list
#cant use max or min

my_list = [78,65,89,86,55,91,64,89]

new_list = []
for i in range(len(my_list)):
    if my_list[i] > my_list[0]:
        new_list.append(my_list[i])
        break
    else:
        i += 1
print(new_list)
    



# print(f'The highest score in class is: {x}')
