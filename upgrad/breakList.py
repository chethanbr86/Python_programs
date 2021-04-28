my_list = [[1,2,3,4,5,6,7,8,9,10,11],3]
j = my_list[0]
k = my_list[1]

for i in range(0,len(j),k):
    print(j[i:i+k])