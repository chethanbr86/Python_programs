# https://www.codechef.com/problems/NAME1

from itertools import chain

t = int(input())
parents = list(map(str, input().split()))
no_child = int(input())
children = list(map(str, input().split()))

print(t, parents, no_child, children)

#myway - finding length of each list element and summing it up
def total_len(df):
    total = 0
    for i in df:
        total = total + len(i)
    return total

# print(total_len(parents))
# print(total_len(children))

par_spell = []
for i in parents:
    par = []
    for j in i:
        par.append(j)
    # print(par)
    par_spell.append(par)
# print(par_spell)

# alpha = list(chain.from_iterable(par_spell))
#or
alpha = [j for i in par_spell for j in i]
# print(alpha)

# if total_len(parents) <= total_len(children):
#     print('NO')
# else:
    