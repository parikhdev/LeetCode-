def twoSum(numbers, target):
        n = len(numbers)
        left = 0
        right = n-1
        while left < right:
            Sum = numbers[left] + numbers[right]
            if Sum == target:
                return [left+1, right+1]
            elif Sum < target:
                left += 1
            else:
                right -= 1
print(twoSum([1,2,3,4,5,6],6))