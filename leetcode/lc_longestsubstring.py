s = 'abcabcbb'
#output = 3 #abc with length of 3

# Below code is just to find substring
l = []
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        l.append(s[i:j])
print(l)

# Real code yet to begin

    

