# https://leetcode.com/problems/binary-search/

# def search(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#     return -1            

# nums = [-1,0,3,5,9,12]
# target = 0             
# print(search(nums, target))

#This is not a if else but a for else problem

#Solving the same by binary search
#leetcode actual solution

def search(numbs, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        middle = left + (right-left)//2
        if nums[middle] == target:
            return middle
        if target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1

nums = [-1,0,3,5,9,12]
target = 9             
print(search(nums, target))