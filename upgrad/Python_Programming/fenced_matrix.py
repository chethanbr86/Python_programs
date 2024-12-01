m,n = 4,5

final = [0]*n

final = [list(final) for i in range(m)] #how?

for i in range(m):
    for j in range(n):
        if i==0 or j==0 or i==m-1 or j==n-1: #i,j are index positions because of range
            print(i,j)
            final[i][j] = 1
            
for i in final:
    print(i)