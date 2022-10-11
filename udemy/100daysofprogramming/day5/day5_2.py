#Print hightest number in list
#cant use max or min

my_list = [78,65,89,86,55,91,64,89]

# new_list = []
# for i in range(0,len(my_list)):
#     if my_list[i] > my_list[0]:
#         # new_list.append(my_list[i])
#         my_list.pop(0)
#     else:
#         my_list.pop(i)
# print(new_list)
# Try this method

#udemy
score = 0
for i in my_list:
    if i > score:
        score = i
print(f'The highest score in class is: {score}')
