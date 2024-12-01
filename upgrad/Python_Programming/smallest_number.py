my_list = [2, -3, 0, -7, 21]
a = my_list[0]

for i in my_list:
    if i < a:
        a = i
    
print(a)