def findDuplicates(nums):
    counts = [0] * (max(nums) + 1)
    double = []
    for num in nums:
        counts[num] += 1
        if counts[num] == 2:
            double.append(num)
    return double
print(findDuplicates([1,3,5,8,3,2,5]))