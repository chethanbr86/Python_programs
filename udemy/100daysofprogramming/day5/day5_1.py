#Calculate average height without using len or sum
my_list = [140,163,186,173,158,177,149]

total = 0
for i in my_list:
    total += i
print(total)

total_len = 0
for j in my_list:
    total_len += 1 #same as len
print(total_len)

average_height = total/total_len
print(round(average_height,2))
