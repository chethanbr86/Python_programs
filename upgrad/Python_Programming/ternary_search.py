data = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
n = 17  #output 7

def ternary_search(data,k):
    l = 0
    r = len(data) - 1
    
    while l<=r:
        mid1 = int(round(((l/3) + (r*2/3)), 0))     
        mid2 = int(round(((r/3) + (l*2/3)), 0)) 
        
        if n == data[mid1]:
            return mid1
        elif n == data[mid2]:
            return mid2
        elif n < data[mid1]:
            r = mid1 - 1
        elif n > data[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1
    
print(ternary_search(data,n))