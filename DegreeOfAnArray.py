def findShortestSubArray(nums):
    count = {}
    first = {}
    degree = 0
    minLen = float('inf')
    for i, num in enumerate(nums):
        if num not in first:
            first[num] = i
        count[num] = count.get(num, 0) + 1
        if count[num] > degree:
            degree = count[num]
            minLen = i - first[num] + 1
        elif count[num] == degree:
            minLen = min(minLen, i - first[num] + 1)
    return minLen
print(findShortestSubArray([1,2,2,3,1]))