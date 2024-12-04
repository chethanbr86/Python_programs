#Find if the given number is above average of the list

my_list = [[3,7,6,9,10,8,5], 7.5]
m = my_list[0]
n = my_list[1]
#1st time
# def sumoflist(m):
#     total = 0
#     for i in m:
#         total = total + i
#     return total

# # avg = sum(m)/len(m)
    
# avg = sumoflist(m)/len(m)

# if n > avg:
#     print(True)
# else:
#     print(False)

# 2nd time:
#easy way
t = sum(m)/len(m)
print(t)
if n > t:
    print(f'{n} is greater than {t:.2f}.')
else:
    print('No')

#difficult way - calculate avg and sum