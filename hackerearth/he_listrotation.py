k = 2
l = [1, 2, 3, 4, 5]

a = l[0]
new = 0

for i in range(len(l)):
    if l[i] > a:
        temp = l[i]
        l[i] = l[new]
        l[new] = temp
        new += 1

print(l)
#not completed
# https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/