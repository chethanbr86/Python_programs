my_list = input().split()
n = int(my_list[0])
a = int(my_list[1])
x = int(my_list[2])

b = n - a
a = a*[0]
b = b*[1]
arr = a + b

for i in range(len(arr)):
    for j in range(1,len(arr)):
        if arr[i] < arr[j]:
#        for j in range(1,x):
#             i = i - 1
            i, j = j, j+1
print(arr)