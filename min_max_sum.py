#Unsolved

arr = [1,3,5,7,9]


def summing(arr):
    total = 0
    total_del = []
    for i in arr:
        arr.pop(0)
        total_del = total + i 
        print(total)
        print(total_del)
    return total_del

print(summing(arr))
        

# def miniMaxSum(arr):
#     a = arr[0]  
    

# print(miniMaxSum(arr))