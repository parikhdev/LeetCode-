def nextGreaterElement(nums1, nums2):
    List = [-1] * len(nums2)
    stack = []
    for i in range(len(nums2)):
        while stack and nums2[i] > nums2[stack[-1]]:
            List[stack[-1]] = nums2[i]
            stack.pop()
        stack.append(i)
    index_map = {value:index for index,value in enumerate(nums2)}
    List2 = []
    for num in nums1:
        idx = index_map[num]
        List2.append(List[idx])
    return List2
print(nextGreaterElement([2,4,3], [3,2,5,4,1]))