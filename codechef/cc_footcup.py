# https://www.codechef.com/MAY221D/submit/FOOTCUP
t = int(input())
for i in range(t):
    m = list(map(int,input().split()))
    x = m[0]
    y = m[1]
    
    if x == 0 or y == 0 or x != y:
        print('NO')
    else:
        print('YES')
