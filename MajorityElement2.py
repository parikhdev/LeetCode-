def majorityElement(nums):
    target = len(nums)//3
    freq = {}
    val = set()
    for i, num in enumerate(nums):
        freq[num] = freq.get(num,0) + 1
        if freq[num] > target:
            val.add(num)
    return list(val)
print(majorityElement([1,2,3,1,2,3,3]))

        