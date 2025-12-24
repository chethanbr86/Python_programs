n = 24316

rev = 0
while n > 0:
    rev = n%10 + rev*10 #n%10 is the last digit of n
    n = n//10 #n//10 is the remaining digits of n
print(rev)
