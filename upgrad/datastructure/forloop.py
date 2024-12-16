li = [5,3,8,2,4,6,10]

for i in li:
    print(i)
    
for j in range(len(li)):
    print('range is ', j)
    print('number is', li[j])
    
for i in range(len(li)):
    for j in range(len(li)):
        print(i, li[i], j, li[j])
        
for i in range(len(li)):
    for j in range(len(li)):
        print(i, li[i], j, li[j])
        
sum_list = 0
for i in li:
    sum_list = sum_list + i
print(sum_list)
