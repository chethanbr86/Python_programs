def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        else:
            return -1

nums = [-1,0,3,5,9,12]
target = 5             
print(search(nums, target))

#not solved yet
