t = int(input())
for i in range(t):
    z = list(map(int,input().split()))
    x = z[0]
    y = z[1]*30
    
    if x < y:
        print('NO')
    else:
        print('YES')