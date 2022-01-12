
#1st method
# import random
# print('[-------------]')
# print('[-----',random.randint(1,6),'-----]')
# print('[-------------]')

# 2nd method
# import random
# def roll(s,e):
#     print(random.randint(1,6))

# s = int(input())
# e = int(input())
# print(roll(s,e))

# 3rd method
# import random
# r = random.randint(1,6)
# print(r)

# for i in range(r+1):
#     if r == 1:
#         print('one')
#         break
#     print('other')
#     break

# Final sol: #myway #not complete
# import random
# r = random.randint(1,6)
# print(r)

# for i in range(1,r+1):
#     if r == 1:
#         print('----------')
#         print('|        |')
#         print('|  ',r*'0','   |')
#         print('|        |')
#         print('----------')
#     #     print(i)
#     #     break
#     # print('None')
#     # break
#     if r == 2:
#         print('----------')
#         print('|        |')
#         print('|  ',r*'0','   |')
#         print('|        |')
#         print('----------')
#     if r == 3:
#         print('----------')
#         print('|        |')
#         print('|  ',r*'0','   |')
#         print('|        |')
#         print('----------')
#     if r == 4:
#         print('----------')
#         print('|        |')
#         print('|  ',r*'0','   |')
#         print('|        |')
#         print('----------')
#     if r == 5:
#         print('----------')
#         print('|        |')
#         print('|  ',r*'0','   |')
#         print('|        |')
#         print('----------')
#     if r == 6:
#         print('----------')
#         print('|        |')
#         print('|  ',r*'0','   |')
#         print('|        |')
#         print('----------')
#         break

# Udemy method:
import random
x = 'y'

while x == 'y':
    r = random.randint(1,6)

    if r == 1:
        print('----------')
        print('|        |')
        print('|    0   |')
        print('|        |')
        print('----------')
    if r == 2:
        print('----------')
        print('|        |')
        print('| 0    0 |')
        print('|        |')
        print('----------')
    if r == 3:
        print('----------')
        print('|    0   |')
        print('|    0   |')
        print('|    0   |')
        print('----------')
    if r == 4:
        print('----------')
        print('| 0    0 |')
        print('|        |')
        print('| 0    0 |')
        print('----------')
    if r == 5:
        print('----------')
        print('| 0    0 |')
        print('|    0   |')
        print('| 0    0 |')
        print('----------')
    if r == 6:
        print('----------')
        print('| 0    0 |')
        print('| 0    0 |')
        print('| 0    0 |')
        print('----------')
    x = input('y or n')