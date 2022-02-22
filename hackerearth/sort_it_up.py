#Asked by microsoft and facebook 
#sove by time complexity 0(n)

# https://www.hackerearth.com/practice/interviews/

arr = [2,1,0,2,0] #list(map(int,input().split(',')))
# print(sorted(arr))
arr_new = []
for i in range(len(arr)):
    if arr[0] >= arr[-1]:
        arr_new.append(arr[0])
        arr.pop(0)
    else:
        arr_new.append(arr[-1])
        arr.pop(-1)
print(arr_new)
#solve using for loop, while loop and use function
