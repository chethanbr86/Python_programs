t = int(input())
for i in range(t):
    m = list(map(int, input().split()))
    p1 = m[0]
    p2 = m[1]
    q1 = m[2]
    q2 = m[3]

    if max(p1,p2) > max(q1,q2):
        print('Q')
    if max(p1,p2) < max(q1,q2):
        print('P')   
    if max(p1,p2) == max(q1,q2):
        print('TIE') 