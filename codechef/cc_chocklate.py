t = int(input())
for i in range(t):
    m = list(map(int, input().split()))
    x = m[0]
    y = m[1]
    z = m[2]

    money = 5*x + 10*y
    choc = 0
# print(money)

    if z <= money :
        choc = choc + money//z
        # print(choc)
    print(choc)