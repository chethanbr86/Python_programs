# https://www.codechef.com/APRIL221C/problems/WATERCOOLER2
t = int(input())
for i in range(t):
    x = list(map(int, input().split()))
    cost_month = x[0]
    total_cost = x[1]
    
    if total_cost//cost_month > 1:
        print(total_cost//cost_month)
    else:
        print(0)