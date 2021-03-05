#Unsolved

arr = [1,3,5,7,9]

def miniMaxSum(arr):
    a = arr[0]
    total = 0
    for i in arr:
        if i < a:
            a = i
        total = sum(arr.pop(a))
    return total

print(miniMaxSum(arr))