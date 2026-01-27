def checkSubarraySum(nums, k):
        curr_sum = 0
        remainder_hist = {0:-1}
        for i, num in enumerate(nums):
            curr_sum += num
            remainder = curr_sum % k
            if remainder in remainder_hist:
                if i - remainder_hist[remainder] >= 2:
                    return True
            else:
                remainder_hist[remainder] = i
        return False
print(checkSubarraySum([0,0,1,2,3,0], 5))