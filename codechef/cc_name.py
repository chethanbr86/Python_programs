# https://www.codechef.com/problems/NAME1

from itertools import chain

t = int(input())
parents = list(map(str, input().split()))
no_child = int(input())
children = list(map(str, input().split()))

# print(t, parents, no_child, names)

#myway - finding length of each list element and summing it up
def total_len(df):
    total = 0
    for i in df:
        total = total + len(i)
    return total

# print(total_len(parents))
# print(total_len(children))

par_spell = chain.from_iterable([parents])


print(par_spell)

# if total_len(parents) <= total_len(children):
#     print('NO')
# else:


