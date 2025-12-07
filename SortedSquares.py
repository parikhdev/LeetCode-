def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    res = []
    
    while right >= left:
        if abs(nums[left]) > abs(nums[right]):
            res.append(nums[left]**2) 
            left += 1
        else:
            res.append(nums[right]**2) 
            right -= 1
    return res[::-1]
    
print(sortedSquares([-8,-4,0,3,10]))