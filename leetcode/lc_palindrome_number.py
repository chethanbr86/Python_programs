n = int(input())

def reverse(n):
    rev = 0
    while n>0:
        rev = rev*10 + n%10
        n = n//10
    return rev

print(reverse(n))
if n == reverse(n):
    print('Palindrome number')
else:
    print('Not a Palindrome number')
    
    