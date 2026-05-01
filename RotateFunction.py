def maxRotateFunction(nums):
    n = len(nums)
    total_sum = sum(nums)
    
    current_f = sum(i * val for i, val in enumerate(nums))
    max_f = current_f

    for i in range(1, n):
        current_f = current_f + total_sum - n * nums[n - i]
        if current_f > max_f:
            max_f = current_f
            
    return max_f
print(maxRotateFunction([4,3,2,6]))