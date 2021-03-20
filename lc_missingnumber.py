def missingNumber(nums):
    nums.sort()
    #print(nums[0])
        
    if nums[0] != 0:
        return 0
    else:
        if nums[-1] == len(nums):
            for i in range(len(nums)):            
                if ((i+1) - i) != 1 or (i - (i-1)) != 1:            
                    break
            return nums[i]-1 #if i not in nums else 'no error'        
        else:
            return nums[-1]+1
           
print(missingNumber([0,3,2]))

#Yet to solve

#leetcode method but not giving right answer
#     if nums[-1] != len(nums):
#         return len(nums)
#     # Ensure that 0 is at the first index
#     elif nums[0] != 0:
#         return 0

#     for i in range(1, len(nums)):
#         expected_num = nums[i-1] + 1
#     if nums[i] != expected_num:
#         return expected_num

# print(missingNumber([0,3,2]))