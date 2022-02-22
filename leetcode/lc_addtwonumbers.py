l1 = [1,0,8]
l2 = [6,9,1]
#output = [7,9,8]

# def addNum(l1,l2):
#     total = []
#     # t2 = 0
#     if len(l1) < len(l2):
#         l1.append(0)
#     else:
#         l2.append(0)
#     print(l1,l2)
#     for i in zip(l1,l2):
#         total.append(sum(i))
#     return total

# print(addNum(l1,l2))

def addNum(l1,l2):
    total = []
    # t2 = 0
    if len(l1) < len(l2):
        l1.append(0)
    else:
        l2.append(0)
    print(l1,l2)
    for i in range(len(l1)):
        total.append(l1[i]+l2[i])
    return total
#in both cases what if l1 == l2?
#And how to know whats the len of linked list to split input and defferentiate between l1 and l2

# l1 = list(map(int,input().split(',')))
# l2 = list(map(int,input().split(',')))
# print(l1)
print(addNum(l1,l2))

