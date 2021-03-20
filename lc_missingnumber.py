def missingNumber(nums):
    nums.sort()
    #print(nums[0])
    
    # for i in range(len(nums)):            
    #     if ((i+1) - i) != 1:            
    #         break
    # return nums[i]-1
    
    if nums[0] != 0:
        return 0
    else:
        if nums[-1] == len(nums):
            for i in range(len(nums)):            
                if ((i+1) - i) != 1 or (i - (i-1)) != 1:            
                    break
            return nums[i] if i not in nums else 'no error'        
        else:
            return nums[-1]+1
           
print(missingNumber([0,3,2]))

#Yet to solve