def longestConsecutive(nums):
    num_set = set(nums)
    maxLength = 0
    for num in num_set:
        if (num - 1) not in num_set:
            length = 1
            current = num
            while (current + 1) in num_set:
                current += 1
                length += 1
            maxLength = max(maxLength, length)
    return maxLength
print(longestConsecutive([1,5,6,8,9,10,11,12,14]))