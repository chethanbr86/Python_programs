# from geeksforgeeks

# my_list = [1,2,3,4,5]
# k = 2

# new_list = []
# for i,x in enumerate(my_list):
#     new_list.append(my_list[(i+3)%len(my_list)])
# print(new_list)

# Learn how to take input from hackerearth problem
#1
#5 2 
#1 2 3 4 5
# Required solution to the problem
# 4 5 1 2 3 not [4,5,1,2,3]

#myway with help

# This is the answer to the above question
n = int(input())
for i in range(n):
    m = list(map(int,input().split()))
    my_list = list(map(int,input().split()))

len_list = m[0]
k = m[1]

new_list = []
# for j in range(n):
for i,x in enumerate(my_list):
    new_list.append(my_list[(i+(k+1))*n%len_list])

# for j in range(n+1):
#     for i,x in enumerate(my_list):
#         new_list.append(my_list[(i+(k+1))*j%len_list])

# print(new_list)
# This is how we provide required solution without list
# for i in range(n):
print(*new_list, sep = " ")

#Solution not according to question page
# https://www.hackerearth.com/practice/codemonk/