def moveZeroes(nums):
    j = 0
    for num in nums:
      if num != 0:
        nums[j] = num
        j += 1
    for i in range(j, len(nums)):
      nums[i] = 0
    return nums

print(moveZeroes([0,3,0,0,9,8,0,0,1]))