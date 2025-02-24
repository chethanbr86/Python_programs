t = int(input().strip())

list_a = [] #1st method of saving
for i in range(t):
    n = int(input().strip())
    a = list(map(int,input().strip().split(',')))
    list_a.append(a)
# print(list_a)

for sub_list in range(len(list_a)):
    for l in range(len(sub_list)):
        if l[0] > l[1]:
            sub_list.pop(l[0])
        else:
            l[1] - l[0]
        
print(list_a)
#not solved