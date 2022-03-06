# https://practice.geeksforgeeks.org/contest/gfg-mega-contest-qualification-round/problems/#
t = int(input())
for i in range(t):
    x = list(map(int,input().split()))
    def split(x):
        for j in x:
            return j

    num_list = list(map(int,str(split(x))))
    print(num_list)
    num = list(map(lambda x:x**4, num_list))
    print(num)

    sum_total = sum(num)
    print(sum_total)    

    def prod(num):
        result = 1
        for k in num:
            if k > 0:
                result = result * k
        return result

    def gcd(a,b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return gcd(a%b, b)
        return gcd(a, b%a)

    z = gcd(sum_total,prod(num))
    if z > 1:
        print(split(x), ' is a special number')
    else:
        print(split(x), ' is not a special numnber')

    #Need to print special numbers in range of split(x)

        

