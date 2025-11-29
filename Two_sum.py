def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        seen[nums[i]] = i
 
    for i in range(len(nums)):
        y = target - nums[i]
 
        if y in seen and seen[y] != i:
            return [i, seen[y]]

print(twoSum([2,7,11,15], 18))
