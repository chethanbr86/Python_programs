str_set = 'figehaeci'
sub_str = {'a','e','i'}
# sub_list = list(sub_str)
sub_list = ['a','e','i']

print(type(sub_str))

#For loop testing
# for i in sub_str:
#     if i in sub_str:
#         print('Yes',i)
#     else:
#         print('No',i)

#This works but go to next one for changes
# count_outer = 0
# count_inner = 0
# #Since we need an index from which everything needs to be printed, lets use range
# for i in range(len(sub_list)):    
#     count_outer += 1
#     for j in range(len(str_set)):
#         count_inner += 1
#         if sub_list[i] == str_set[j]:
#             print('Yes',str_set[i:],i,j)
#         # else:
#         #     print('No')
# print(count_inner)
# print(count_outer)

count_outer = 0
count_inner = 0
#Since we need an index from which everything needs to be printed, lets use range
for i in range(len(sub_list)):    
    count_outer += 1
    for j in range(len(str_set)):
        count_inner += 1
        if sub_list[i] == str_set[j]:
            break
print('Yes',str_set[j:],i,j)
        # else:
        #     print('No')
print(count_inner)
print(count_outer)
#This one actually works but not as the problem wanted, check once.