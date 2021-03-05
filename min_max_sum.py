#Unsolved

arr = [1,3,5,7,9]


def summing(arr):
    total = []

    for i in arr:
        
        total.append(sum(arr.pop(0))) 

    return total

print(summing(arr))
        

# def miniMaxSum(arr):
#     a = arr[0]  
    

# print(miniMaxSum(arr))