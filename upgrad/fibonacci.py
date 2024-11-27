n = 6

l, sl = 1, 0

if n>0:
    print(sl)
if n>1:
    print(l)
for i in range(3,n+1):
    fib = l + sl
    print(fib)
    sl = l
    l = fib

#using codium
# def fib(n):
#     fibo=[1]*(n+1)
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         for i in range(2, n+1):
#             fibo[i]=fibo[i-1] + fibo[i-2]
#         return fibo[n-1]        

# print(fib(6))