# https://www.codechef.com/START45D?order=desc&sortBy=successful_submissions
# https://www.codechef.com/START45D/problems/CHEFAPPS

# t = int(input())
# for i in range(t):
#     w = list(map(int,input().split()))
#     S = w[0]
#     X = w[1]
#     Y = w[2]
#     Z = w[3]
    
#     total = X+Y
#     if total + Z <= S:
#         print(0)
#     else:
#         if total <= Z:
#             print(2)
#         elif total - Y + Z <= S or total - X + Z <= S:
#             print(1)

t = int(input())
for i in range(t):
    w = list(map(int,input().split()))
    S = w[0]
    X = w[1]
    Y = w[2]
    Z = w[3]
    
    total = X+Y+Z
    if total <= S:
        print(0)
    elif total - X <= S or total - Y <= S:
        print(1)
    else:
        print(2)

#not complete