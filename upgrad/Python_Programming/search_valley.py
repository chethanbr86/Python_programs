valley_list= [13, 11, 8, 7, 6, 4, 3, 2, 1, 14, 15, 16, 17]
key=8  #output 2

def valley_array(valley_list,key):
    l = 0
    r = len(valley_list) -1
    while l<=r:
        mid=(l+r)//2

        if valley_list[mid] == key:
            return mid
        elif valley_list[l] >= valley_list[mid]:
            if key <= valley_list[l] and key > valley_list[mid]:
                r = mid - 1
            else:
                l = mid + 1
        elif valley_list[l] < valley_list[mid]:
            if key > valley_list[mid] and key <= valley_list[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

print(valley_array(valley_list,key))