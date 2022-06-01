# https://www.codechef.com/START41D/problems/INCREAR
t = int(input())
for i in range(t):
    m = list(map(int, input().split()))
    x = m[0]
    y = m[1]

    # if x == y:
    #     print(0)
    # else:
    count_x = 0
    count_y = 0
    while x == y:        
        count_x += 1
        count_y += 1
        x = x + 1
        y = y + 2
    print(count_x+count_y)
        


#not solved yet



            

