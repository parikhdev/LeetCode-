from collections import defaultdict
def subarraysWithKDistinct(nums, k):
    def atMostK(nums, k):
        count = defaultdict(int)
        res = left = 0
        for right, num in enumerate(nums):
            if count[num] == 0:
                k -= 1
            count[num] += 1
            while k < 0:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    k += 1
                left += 1
            res += right - left + 1
        return res
    return atMostK(nums, k) - atMostK(nums, k-1)
print(subarraysWithKDistinct([1,2,1,2,3],2))
