n = 5

def prime(p):    
    for i in range(2,p):
        if p%i == 0:
            return False
    return True

total = 0    
for i in range(2,n+1):
    if prime(i):
        total = total + i
        print(i)

print(total)
