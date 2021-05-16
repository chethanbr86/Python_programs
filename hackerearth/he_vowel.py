# hackerearth solution

def solve(s):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    flag1 = True
    flag2 = True
    for i in vowels:
        if i not in s:
            flag1 = False
        if i.upper() not in s:
            flag2 = False
    return flag1 or flag2
 
n = int(input())
for i in range(n):
    s = input()
    if solve(s):
        print("lovely string")
    else:
        print("ugly string")

#myway
'''
def vowel(name):    
    vow = 'aeiou'
    flag1 = True
    flag2 = True
    for i in vow:
        if i in name:
            flag1 = True 
        if i.upper() in name:
            flag2 = True
    return flag1 or flag2

m = int(input())
for i in range(m):
    name = input()
    if vowel(name):
        print('lovely string')
    else:
        print('ugly string')
'''
#unsolved