def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1            

nums = [-1,0,3,5,9,12]
target = 0             
print(search(nums, target))

#This is not a if else but a for else problem
