t = int(input().strip())

list_a = [] #1st method of saving
for i in range(t):
    n = int(input().strip())
    a = list(map(int,input().strip().split(',')))
    list_a.append(a)
print(list_a)

# for i in list_a:
#     max_element = i[0]
#     for j in i:
#         if j > max_element:
#             max_element = j
#         else:            
#             i.remove(j)
#     print(max_element)

for i in list_a:
    # max_element = i[0]
    for j in range(len(i)-1):
        if i[j] > i[j+1]:
            i[j] - i[j+1]
            i.remove(i[j+1])
        # else:            
        #     j[1] - j[0]
        #     i.remove(j[1])
    # print(max_element)

print(list_a)

#not completed
        
