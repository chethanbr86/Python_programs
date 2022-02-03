def swap(l1,p1,p2):
    l1[p1],l1[p2] = l1[p2],l1[p1]
    return l1

inp = [23, 65, 19, 90]
pos = list(map(int,input().split(',')))
p1 = pos[0]
p2 = pos[1]

# for i in pos: #no need of for loop
if p1 > len(inp) or p1 < 1 or p2 > len(inp) or p2 < 1: 
    print('Input again')
else:
    print('Solution is:', swap(inp,p1-1,p2-1))