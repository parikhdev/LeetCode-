def findLengthOfLCIS(nums):
    if not nums:
        return 0
    length = 0
    left = 0
    for right in range(len(nums)):
        if right > 0 and nums[right] <= nums[right - 1]:
            left = right
        length = max(length, right - left + 1)
    return length

print(findLengthOfLCIS([1,3,5,4,7]))