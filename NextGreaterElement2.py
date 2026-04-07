def nextGreaterElements(nums):
    n = len(nums)
    stack = [] 
    result = [-1] * n 

    for i in range(n * 2):
        actual_index = i % n 
        curr_num = nums[actual_index]
        while stack and curr_num > nums[stack[-1]]:
            weak_index = stack.pop()
            result[weak_index] = curr_num
        if i < n:
            stack.append(actual_index)

    return result
print(nextGreaterElements([1,2,1]))