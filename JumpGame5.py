def maxJumps(arr, d): 
    n = len(arr)
    dp = [1] * n
    
    sorted_indices = [(arr[i], i) for i in range(n)]
    sorted_indices.sort()
    
    for value, i in sorted_indices:
        
        for j in range(i + 1, min(i + d + 1, n)):
            if arr[j] >= arr[i]:
                break
            dp[i] = max(dp[i], dp[j] + 1)
            
        for j in range(i - 1, max(i - d - 1, -1), -1):
            if arr[j] >= arr[i]:
                break
            dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(maxJumps([6,4,14,6,8,13,9,7,10,6,12],2))