def isGood(nums):
    n = len(nums) - 1
    if n < 1:
        return False
    target = list(range(1, n)) + [n, n]
    return sorted(nums) == target

print(isGood([2, 1, 3]))