#Asked by microsoft and facebook 
#sove by time complexity 0(n)

arr = [2,1,0,2,0] #list(map(int,input().split(',')))
# print(sorted(arr))
arr_new = []
for i in range(len(arr)):
    if arr[-1] < arr[0]:
        arr_new.append(arr[-1])
        arr.pop(-1)
    else:
        arr_new.append(arr[0])
        arr.pop(0)
print(arr_new)
