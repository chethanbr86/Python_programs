# from geeksforgeeks for 1 iteration

# my_list = [1,2,3,4,5]
# k = 2

# new_list = []
# for i,x in enumerate(my_list):
#     new_list.append(my_list[(i+(k+1))%len(my_list)])
# print(new_list)
#Solution correct for 1 iteration

#Learnings:
# Learn how to take input from hackerearth problem
#1
#5 2 
#1 2 3 4 5

#Answer for above question
# n = int(input())
# for i in range(n):
#     m = list(map(int,input().split()))
#     my_list = list(map(int,input().split()))

# This is how we provide required solution without list
# for i in range(n):
#     print(*new_list, sep = " ")
#Learnings end

# Required solution to the problem
# 4 5 1 2 3 not [4,5,1,2,3]
# If iteration is n=2 then: 
# 4 5 1 2 3
# 3 4 5 1 2

#myway with help for multiple iterations
# def monk(l,k):
#     new_list = []
#     for i,x in enumerate(my_list):
#         new_list.append(my_list[(i+(k+1))%len_list])
#     return new_list

# n = int(input())
# for i in range(n):
#     len_list,k = map(int,input().split())
#     my_list = list(map(int,input().split()))

#     g = monk(len_list,k)
#     print(*g, sep = " ")
# Not correct

# Github solution
# n  = int(input())
# for _ in range(n):
#     len_list,k = map(int,input().split())
#     my_list = list(map(int,input().split()))
#     x = k%len_list
#     print(*(my_list[len_list-x:]+my_list[:len_list-x]))
#Not correct

#Solution not according to question page
# https://www.hackerearth.com/practice/codemonk/

