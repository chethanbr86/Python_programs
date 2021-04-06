s1 = 'thing'
s2 = 'night'

# l1 = len(s1)
# l2 = len(s2)

def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1.count(s1[i]) != s2.count(s1[i]): #did not understand funda correctly
            return False
        print(s1[i],s2[i])
        print(s1.count(s1[i]),s2.count(s1[i]))
    return True

print(anagram(s1,s2))
