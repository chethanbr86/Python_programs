L1 = [1, 1, 2, 4, 8, 8, 8, 9]
L2 = [1, 2, 6, 7, 8, 8, 8]
#output [1, 2, 8, 8, 8]

i,j=0,0
L = []

while i<len(L1) and j<len(L2):
    if L1[i] == L2[j]:
        L.append(L1[i])
        i += 1
        j += 1
    elif L1[i]>L2[j]:
        j += 1
    else:
        i += 1
print(L)