def minStartValue(nums):
        curr_sum = 0
        min_prefix = 0
        for num in nums:
            curr_sum += num
            min_prefix = min(min_prefix, curr_sum)
        return 1 - min_prefix
print(minStartValue([-3,2,-3,4,2]))