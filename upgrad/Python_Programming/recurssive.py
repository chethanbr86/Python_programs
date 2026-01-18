n = 12
k = 5
# Output  12, 7, 2, -3, 2, 7, 12

L = []
# Function
def pattern(n,k):
    if (n+k)>0:
        L.append(n)
        pattern(n-k,k)
        if n>0:
            L.append(n)
    else:
        return
pattern(n,k)
o=''
for i in L:
    o = o+', '+str(i)
print(o.strip(','))