# https://www.codechef.com/START41D/problems/INCREAR
t = int(input())
for i in range(t):
    m = list(map(int, input().split()))
    x = m[0]
    y = m[1]

    if x == y:
        print(0)
    else:
        count = 0
        while target%x == 0 or target%y == 0:
            x = x + 1
            y = y + 2
            count += 1
        print(count)

#not solved yet



            

