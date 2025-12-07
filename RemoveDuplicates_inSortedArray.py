def removeDuplicates(nums):
    nums.sort()
    n = len(nums)
    j = 1
    for i in range(1, n):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    
    return nums[:j]

nums = [1,0,8,1,4,3,8,3,0]
print(removeDuplicates(nums)) 
