#1st method:
""" from functools import reduce

n = 5

if n < 0:
    print(-1)
elif n==0:
    print(1)
else:
    fact = reduce(lambda x,y: x*y, range(1,n+1))
    print(fact) """

#2nd method:
""" def fact(n):
    f = 1
    if n < 0:
        return -1
    elif n==0:
        return 1
    else:
        for i in range(1, n+1):
            f = f * i
        return f

print(fact(5)) """

#3rd method:
def fact(n):
    f = 1
    if n < 0:
        return -1
    elif n==0:
        return 1
    else:
        f = n* fact(n-1)
        return f

print(fact(5))
        