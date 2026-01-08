def removeElement(nums, val):
    n = len(nums)
    k = 0
    for i in range(n):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

print(removeElement([1,2,3,4,3,5], 3))
        