#1st method:
from functools import reduce

n = 5

if n < 0:
    print(-1)
elif n==0:
    print(1)
else:
    fact0 = reduce(lambda x,y: x*y, range(1,n+1))
    print(fact0) 

#2nd method:
def fact1(n):
    f = 1
    if n < 0:
        return -1
    elif n==0:
        return 1
    else:
        for i in range(1, n+1):
            f = f * i
        return f

print(fact1(5)) 

#3rd method:
def fact2(n):
    f = 1
    if n < 0:
        return -1
    elif n==0:
        return 1
    else:
        f = n* fact2(n-1)
        return f

print(fact2(5))

#Try using while loop for factorial
        