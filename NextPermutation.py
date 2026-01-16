def nextPermutation(nums):
    n = len(nums)
    pivot_index = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot_index = i
            break
    
    if pivot_index != -1:
        swap_index = -1
        for j in range(n - 1, pivot_index, -1):
            if nums[j] > nums[pivot_index]:
                swap_index = j
                break
        nums[pivot_index], nums[swap_index] = nums[swap_index], nums[pivot_index]
        
    left, right = pivot_index + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

my_list = [1, 2, 3]
nextPermutation(my_list)
print(my_list) 