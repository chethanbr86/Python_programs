data = [5, 6, 7, 10, 16, 17, 19]
key = 24

# output 7 17

l = 0
r = len(data)-1

while l<r:
    if (data[l] + data[r]) == key:
        print(data[l],data[r])
        break
    elif (data[l] + data[r]) < key:
        l = l + 1
    else:
        r = r - 1   