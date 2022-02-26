t = int(input())
for i in range(t):
    x = list(map(int,input().split())) 
    no_of_person = x[0]
    money_units = x[1]
    withdraw = list(map(int,input().split()))
    for j in withdraw: #this is a way of taking input but not storing in any variables but directly accessing from list
        if j <= money_units:
            money_units -= j
        else:
            print('Not enough cash')
    print('Money units left: ',money_units)
