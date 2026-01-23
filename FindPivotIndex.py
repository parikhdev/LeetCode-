def pivotIndex(nums):
        left_sum = 0
        Total = sum(nums)
        for i in range(len(nums)):
            right_sum = Total - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum = left_sum + nums[i]
        return -1
print(pivotIndex([0,1,2,3,4,5,4,3,2,1,0]))