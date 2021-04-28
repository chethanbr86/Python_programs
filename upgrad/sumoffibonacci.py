# n=4
# fib=[1]*(n+1)
# for i in range(2, n+1):
#     fib[i]=fib[i-1] + fib[i-2]
# print(fib[n-1])

def fib(n):
    fibo=[1]*(n+1)
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        for i in range(2, n+1):
            fibo[i]=fibo[i-1] + fibo[i-2]
        return fibo[n-1]

print(fib(7))