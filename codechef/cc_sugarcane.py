# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    total = 50*n
    profit = total - (0.20+0.20+0.30)*total
    print(int(profit))
