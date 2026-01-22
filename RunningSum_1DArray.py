def runningSum(nums):
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
        nums[i] = sum
    return nums
print(runningSum([1,2,3,4,5,6,7,8,9,10]))
    