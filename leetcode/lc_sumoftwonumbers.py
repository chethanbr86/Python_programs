# def twoSum(nums, target):
#     new_list = []
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] + nums[j] == target:
#                 new_list.append(i)
#                 new_list.append(j)
#                 return new_list

# print(twoSum([3,2,4], 6))

def twoSum(nums, target):
    new_list = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                new_list.append(i)
                new_list.append(j)
                return new_list

print(twoSum([3,2,4], 6))

