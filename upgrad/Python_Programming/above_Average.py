my_list = [[2,4,6,8,10,12], 6.5]
m = my_list[0]
n = my_list[1]

def sumoflist(m):
    total = 0
    for i in m:
        total = total + i
    return total

# avg = sum(m)/len(m)
    
avg = sumoflist(m)/len(m)

if n > avg:
    print(True)
else:
    print(False)