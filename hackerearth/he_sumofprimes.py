#sum of primes under 10 or n
t = int(input().strip())
list1 = []
for a0 in range(t):
    n = int(input().strip())
    list1.append(n)

list2 = []
for i in list1:
    if i%2 != 0 or 1%3 !=0 or i%5 != 0 or i%7 == 0:
        list2.append(i)
        i += 1
    else:
        continue

print(sum(list2))
#not working