sorted_list= [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
key= 17  #output 7

def binary_search(sorted_list,key):
    l = 0
    r = len(sorted_list) -1
    while l<=r:
        mid = (l+r)//2
        
        if sorted_list[mid] == key:
            return mid
        elif sorted_list[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
            
    return -1

print(binary_search(sorted_list,key)) 