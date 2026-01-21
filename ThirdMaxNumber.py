def thirdMax(nums):
    highest = float('-inf') 
    secondHighest = float('-inf') 
    thirdHighest = float('-inf') 
    for num in nums:
        if num in (highest,secondHighest,thirdHighest):
            continue
        if num > highest:
            thirdHighest = secondHighest
            secondHighest = highest
            highest = num
        if num > secondHighest and num < highest:
            thirdHighest = secondHighest
            secondHighest = num
        if num > thirdHighest and num < secondHighest:
            thirdHighest = num
    if thirdHighest > float('-inf'):
        return thirdHighest
    else:
        return highest
print(thirdMax([1,3,2,2,4,5,4]))