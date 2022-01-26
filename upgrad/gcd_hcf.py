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

inp = input()
a,b = map(int,inp.split(',')) #imp
print(a,b,type(a),type(b))
if gcd(a,b):
    print('GCD of ', a, 'and', b, 'is', gcd(a,b))
else:
    print('no GCD found')