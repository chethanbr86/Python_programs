s1 = 'abshdksajd'
s2 = 'abshiehand'

l1 = len(s1)
l2 = len(s2)
min_len = min(l1,l2)

for i in range(min_len):
    if s1[i] != s2[i]:
        break

if i == 0:
    print(-1)
else:
    print(s1[:i])
