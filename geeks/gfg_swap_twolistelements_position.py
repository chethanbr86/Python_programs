def swap(l1,p1,p2):
    l1[p1],l1[p2] = l1[p2],l1[p1]
    return l1

inp = [23, 65, 19, 90]
pos = list(map(int,input().split(',')))
# print(pos)
# print(len(inp))
p1 = pos[0]
p2 = pos[1]

for i in pos:
    if i > len(inp) or i < 1:
        print('Input again')
    else: # answer is right but loop being run twice, check and debug
        print('Solution is:', swap(inp,p1-1,p2-1))