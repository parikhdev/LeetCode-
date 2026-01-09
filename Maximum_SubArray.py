def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    # start = 0
    # best_start = 0
    # best_end = 0
    for i in range(1, len(nums)):
        num = nums[i]
        if current_sum < 0:
            current_sum = num
            # start = i
        else:
            current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
            # best_start = start
            # best_end = i
    return max_sum #, nums[best_start:best_end+1]

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4,9]))