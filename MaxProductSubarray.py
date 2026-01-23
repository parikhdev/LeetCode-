def maxProduct(nums):
    max_product = 1
    min_product = 1
    Global_max = float('-inf')
    for i in range(len(nums)):
        x = nums[i]
        if x >= 0:
            max_product = max(x,max_product*x)
            min_product = min(x,min_product*x)
        if x < 0:
            temp = max_product
            max_product = min_product
            min_product = temp
            max_product = max(x, max_product * x)
            min_product = min(x, min_product * x)
        Global_max = max(Global_max, max_product)
    return Global_max
print(maxProduct([-2,0,3,4,5]))
