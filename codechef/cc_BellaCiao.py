#Chef is planning a heist in the reserve bank of Chefland. They are planning to hijack the bank for D days and print the money. The initial rate of printing the currency is P dollars per day and they increase the production by Q dollars after every interval of d days. For example, after d days the rate is P+Q dollars per day, and after 2d days the rate is P+2Q dollars per day, and so on. Output the amount of money they will be able to print in the given period.

t = int(input())
for i in range(t):
    x = list(map(int,input().split()))
    D = x[0]
    d = x[1]
    P = x[2]
    Q = x[3]
    
    for i in range(1,D+1):
        for j in range(1,d+1):
            if i < j:
                P = P
            if i >= j:
                P = P + j*Q
                
    print(P)     

                