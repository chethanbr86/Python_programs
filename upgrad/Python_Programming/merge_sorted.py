m1 = [1, 3, 5, 7, 9, 10]
m2 = [2, 3, 4, 5, 6, 8, 11, 12, 13]

#output [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]

m = []
i=0
j=0

while i<len(m1) and j<len(m2): 
    if m1[i] < m2[j]:
        m.append(m1[i])
        i=i+1
    else:
        m.append(m2[j])
        j=j+1
        
m = m + m1[i:] + m2[j:]
            
print(m)