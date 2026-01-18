L = [1, 3, 5, 6, 10]
k = 8  #output No

l = 0
r = len(L) - 1

def diff_fun(L,k,l,r):
    while (l<r):
        if (L[r] - L[l]) == k:
            return 1
        elif (L[r] - L[l]) < k:
            l = l + 1            
        else:
            r = r - 1 
            
z = diff_fun(L,k,l,r)          
if z == 1:
    print('Yes')
else:
    print('No')