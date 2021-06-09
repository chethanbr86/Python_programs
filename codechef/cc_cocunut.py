#Chefland has 2 different types of coconut, type A and type B. Type A contains only xa milliliters of coconut water and type B contains only xb grams of coconut pulp. Chef's nutritionist has advised him to consume Xa milliliters of coconut water and Xb grams of coconut pulp every week in the summer. Find the total number of coconuts (type A + type B) that Chef should buy each week to keep himself active in the hot weather.

# new method of taking multiple input other the the one used below
'''
t = int(input())
my_list = []
for _ in range(t):
    inp = input().split(' ')
    new_list = [int(s) for s in inp]
    my_list.append(new_list)    
print(my_list)

t = int(input())
#lis = []
for i in range(t):
    x = list(map(int,input().split(' ')))
    #lis.append(x)
    #x = input().split(' ')  #if the above code doesn't work
    x1 = int(float(x[0]))
    x2 = int(float(x[1]))
    total_a = int(float(x[2]))
    total_b = int(float(x[3]))
    #print(x)
    #print(type(x[2]))

    x1 = x[0]
    x2 = x[1]
    total_a = x[2]
    total_b = x[3]
    #print(x1,x2,x3,x4)
    
#def coconut(x1,x2,total_a,total_b):
    a = total_a/x1
    b = total_b/x2
    c = int(a+b)
    print(c)

while True:
    try:
        t = int(input())
        for i in range(t):
            # x = list(map(int,input().split(' ')))
            x = input().split(' ')
            x1 = int(float(x[0]))
            x2 = int(float(x[1]))
            total_a = int(float(x[2]))
            total_b = int(float(x[3]))
            a = total_a/x1
            b = total_b/x2
            c = int(a+b)
            print(c)
    except EOFError as e:
        print (e)
        break
'''   
#Getting right answer in all above but not in codechef because of input

#Submitted solution
t = int(input())
for i in range(t):
    x = input().split()
    x1 = int(float(x[0]))
    x2 = int(float(x[1]))
    total_a = int(float(x[2]))
    total_b = int(float(x[3]))
    # x = list(map(int,input().split()))
    # x1 = x[0]
    # x2 = x[1]
    # total_a = x[2]
    # total_b = x[3]
    a = total_a/x1
    b = total_b/x2
    c = int(a+b)
    print(c)