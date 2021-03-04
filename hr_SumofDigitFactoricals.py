#Here we are using one function inside another function

from functools import reduce

# num = 351

#myway
# num_list = list(map(int, str(num)))
# print(num_list)

#otherway
# def split_num(n):
#     s = list(str(n))
#     return [int(i) for i in s]

#mishmash
def split_num(n):
    return list(map(int, str(n)))

print(split_num(342))

#myway
# fact1 = reduce(lambda x, y: x*y, range(1, num_list[0]+1))
# fact2 = reduce(lambda x, y: x*y, range(1, num_list[1]+1)) 
# total = fact1+fact2
# print(total)

#otherway
# def fact(n):
#     if n > 1:
#         return n*fact(n-1)    
#     else:
#         return 1

#mishmash
def fact(n):
    if n > 1:
        return reduce(lambda x,y: x*y, range(1,n+1))   
    else:
        return 1

#myway
# sum = 0
# num_list2 = list(map(int, str(total)))
# for i in num_list2:
#     sum += i
# print(sum)

#otherway
def f(n):
    return sum([fact(k) for k in split_num(n)])    #return sum([fact(k) for k in num_list]) #if myway is used at start

print(f(342))

def sf(n):
    return sum(split_num(n))

print(sf(f(342)))

#credit charlesreid1
def g(p):
    n = 1
    sf_val = sf(n)
    while sf_val != p:
        n+=1
        sf_val = sf(n)
    return n

def sg(p):
    return sum(split_num(g(p)))

