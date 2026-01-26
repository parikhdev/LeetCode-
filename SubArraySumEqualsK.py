def subarraySum(nums, k):
    currSum = 0
    count = 0 
    history = {0:1}
    for num in nums:
        currSum += num
        if currSum - k in history:
            count += history[currSum - k]
        history[currSum] = history.get(currSum, 0) + 1
    return count
        
print(subarraySum([1,-1,3,0,0,-3,4,5], 0))