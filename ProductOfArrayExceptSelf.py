def productExceptSelf(nums):
        n = len(nums)
        res = [1] * n
        rightProd = 1
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        for i in range(n-1,-1,-1):
            res[i] *= rightProd
            rightProd *= nums[i]
        return res
print(productExceptSelf([1,2,3,4,5]))