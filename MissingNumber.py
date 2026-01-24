def missingNumber(nums):
        nums_set = set(nums)
        for i in range(len(nums)):
            if i not in nums_set:
                return i
        return len(nums)
print(missingNumber([1,0,6,4,3,2]))