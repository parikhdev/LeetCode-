def minElement(nums): 
    return min(sum(int(digit) for digit in str(num)) for num in nums)

print(minElement([10,12,13,14]))