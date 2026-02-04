def trap(height):
    n = len(height)
    left, right = 0, n-1
    left_Max = right_Max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_Max:
                left_Max = height[left]
            else:
                water += left_Max - height[left]
            left += 1
        else:
            if height[right] >= right_Max:
                right_Max = height[right]
            else:
                water += right_Max - height[right]
            right -= 1
    return water
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))
