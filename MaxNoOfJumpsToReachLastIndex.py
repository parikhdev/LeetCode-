def maximumJumps(nums, target):
    n = len(nums)
    dp = [-1] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[-1]

print(maximumJumps([1,3,6,4,1,2], 2))