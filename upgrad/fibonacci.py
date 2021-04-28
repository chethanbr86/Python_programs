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
        