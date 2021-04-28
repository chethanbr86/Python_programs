from above_Average import sumoflist

my_list = [[2,4,6,8,10,12], [6.5,7.5]]
m = my_list[0]
n = my_list[1]

def check_avg(m,n):
    avg = sumoflist(m)/len(m)
    if n > avg:
        return 1
    else:
        return 0

for j in n:
    is_add = check_avg(m,j)
    if is_add == 1:
        m.append(j)

print(m)


