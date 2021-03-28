# Upgrad solution
n=6
pascal = [[1 for i in range(i)] for i in range(1,n+1)]

for i in range(2,n):
    for j in range(1,i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        
print(pascal[-1])
print(pascal)