# cook your dish here
t = int(input())
for i in range(t):
    m = list(map(int,input().split()))
    x = m[0]
    y = m[1]
    
    if y <= 1.07*x:
        print('YES')
    else:
        print('NO')
