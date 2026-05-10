n = int(input())
#It is conjectured that every positive integer eventually reaches 1, eg: 6, 3, 10, 5, 16, 8, 4, 2, 1
n_list= []
# i = 0

while n != 1:
    if n%2 == 0:
        n = n//2
        n_list.append(n)
        if n == 1:
            break
    else:
        n = 3*n + 1
        n_list.append(n)
        if n == 1:
            break

print(n_list)

#Got it right in first try

