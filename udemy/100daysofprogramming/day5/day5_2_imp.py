#Print hightest number in list
#cant use max or min

my_list = [78,65,89,86,55,91,64,89]

#myway
# new_list = []
# for i in range(0,len(my_list)):
#     if my_list[i] > my_list[0]:
#         # new_list.append(my_list[i])
#         my_list.pop(0)
#     else:
#         my_list.pop(i)
# print(new_list)

#udemy
high_score = 0
for current_score in my_list:
    if current_score > high_score:
        high_score = current_score
print(f'The highest score in class is: {high_score}')
