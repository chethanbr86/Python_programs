# 2 #total 2 cycles of inputs
# 5 10 #1st cycle stored in variables
# 3 5 3 2 1 #1st cycle accessing directly
# 4 6 #2nd cycle same as above
# 10 8 6 4 2nd cycle same as above
# sol:
# 11010
# 0010

#myway - except for input way
# t = int(input())
# for i in range(t):
#     # x = list(map(int,input().split())) 
#     # no_of_person = x[0]
#     # money_units = x[1]
#     no_of_person, money_units = list(map(int,input().split())) #check
#     print(f'no_of_person: {no_of_person}, money_units: {money_units}')
#     withdraw = list(map(int,input().split()))
#     print(f'withdraw: {withdraw}')
#     for j in withdraw: #this is a way of taking input but not storing in any variables but directly accessing from list
#         if j <= money_units:
#             money_units -= j
#             print(1, end='\n')
#             print(f'money_units after success: {money_units}')
#         else:
#             print(0, end='\n')
#             print(f'money_units after failure: {money_units}')

#without comments and condition
# t = int(input())
# for i in range(t):
#     no_of_person, money_units = list(map(int,input().split())) 
#     withdraw = list(map(int,input().split()))
#     for j in withdraw: 
#         if j <= money_units:
#             money_units -= j
#             print(1, end='')
#         else:
#             print(0, end='')

#with condition - accepted
t = int(input())

while t:     
    t -= 1    
    no_of_person, money_units = list(map(int,input().split()))
    withdraw = list(map(int,input().split()))    
    if len(withdraw) != no_of_person:
        print('wrong entry')
        continue
    else:
        for j in withdraw: 
            if j <= money_units:
                money_units -= j
                print(1, end='')
            else:
                print(0, end='')
    print('\n')
    

