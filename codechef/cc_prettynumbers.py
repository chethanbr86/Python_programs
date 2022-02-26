#print the numbers which ends with 2,3,9 within a given range   
t = int(input())
for i in range(t):
    x = list(map(int,input().split())) #For a split like this, space is the separator
    l1 = x[0]
    l2 = x[1]
    print(t,x,l1,l2)
    
    new_list=[]
    for i in range(l1,l2+1):
        if i%10 == 2 or i%10 == 3 or i%10 == 9:
            new_list.append(i)
    print(new_list)

# def inp(t):
#     t = int(input())
#     for i in range(t):
#         x = list(map(int,input().split())) #For a split like this, space is the separator
#         l1 = x[0]
#         l2 = x[1]
#     return [l1,l2]
# print(inp(2))
# #not sure how to take input using function and feed it to another function





