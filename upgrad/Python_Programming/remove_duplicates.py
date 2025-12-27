l1 = [8,9,2,2,3,4,5,2]

l2= {}

for i in l1:
    if i not in l2:
        l2[i] = i
        print(l2)
print(list(l2.keys()))