def searchInsert(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    if nums[m] < target:
        return m + 1
    else:
        return m

print(searchInsert([1,3,5,9], 7))