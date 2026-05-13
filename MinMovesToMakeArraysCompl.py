def minMoves(nums, limit): 
    n = len(nums)
    diff = [0] * (2 * limit + 2)
    
    for i in range(n // 2):
        a, b = nums[i], nums[n - 1 - i]
        
        min_val = min(a, b)
        max_val = max(a, b)
        
        diff[2] += 2
        diff[min_val + 1] -= 1
        diff[a + b] -= 1
        diff[a + b + 1] += 1
        diff[max_val + limit + 1] += 1
        
    ans = n
    curr_moves = 0
    for s in range(2, 2 * limit + 1):
        curr_moves += diff[s]
        ans = min(ans, curr_moves)
        
    return ans

print(minMoves([1,2,4,3],4))