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
def avg_calculation(list2):
    t = sum(list2)/len(list2)
    print(t)
    if n > t:
        print(f'{n} is greater than {t}.')
    else:
        print('No')

avg_calculation(m)

#difficult way - calculate avg and sum

# Note: Avoid range(len(list)) unless you need fine-grained control over indices or are working with multiple lists.

# total = 0
# for i in range(len(m)):
#     total = total + m[i]
# print(total)
# class Calculation:

def avg_cal(list1):        
    total = 0
    avg = 0
    for i in list1:
        total = total + i
        avg = total/len(list1)
    return avg        

if n > avg_cal(m):
    print(f'{n} is greater than {avg_cal(m)}.')
else:
    print('No')
