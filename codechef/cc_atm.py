# 2 #total 2 cycles of inputs
# 5 10 #1st cycle stored in variables
# 3 5 3 2 1 #1st cycle accessing directly
# 4 6 #2nd cycle same as above
# 10 8 6 4 2nd cycle same as above
# sol:
# 11010
# 0010

t = int(input())
for i in range(t):
    x = list(map(int,input().split())) 
    no_of_person = x[0]
    money_units = x[1]
    withdraw = list(map(int,input().split()))
    for j in withdraw: #this is a way of taking input but not storing in any variables but directly accessing from list
        if j <= money_units:
            money_units -= j
            print(1, end='')
        else:
            print(0, end='')