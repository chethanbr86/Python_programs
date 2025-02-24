t = int(input().strip())

list_a = [] #1st method of saving
for i in range(t):
    n = int(input().strip())
    a = list(map(int,input().strip().split(',')))
    list_a.append(a)
print(list_a)

