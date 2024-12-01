#From rookieslab
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a = [4, 10, 16, 14]

result = a[0]
for i in a[1:]:
    result = gcd(result, i)

print(result)