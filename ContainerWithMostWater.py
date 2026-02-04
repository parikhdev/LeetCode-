def maxArea(height):
    n = len(height)
    max_area = 0
    left = 0
    right = n-1
    for i in range(n):
        if (height[left] < height[right]):
            area = min(height[left],height[right]) * (right - left)
            left += 1
        else:
            area = min(height[left],height[right]) * (right - left)
            right -= 1
        max_area = max(max_area, area)
    return max_area


print(maxArea([1,8,6,2,5,4,8,3,7]))   
