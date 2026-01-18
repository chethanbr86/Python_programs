data = [15, 16, 17, 18, 11, 12, 13, 14]
key = 12  #output 5

def rotated_array(data,key):
    l = 0
    r = len(data) -1
    while l<=r:
        mid=(l+r)//2

        if data[mid] == key:
            return mid
        elif data[l] <= data[mid]:
            if key>=data[l] and key<data[mid]:
                r = mid - 1
            else:
                l = mid + 1
        elif data[l] > data[mid]:
            if key>data[mid] and key <= data[r]:
                l=mid+1
            else:
                r=mid-1
    return -1

print(rotated_array(data,key))