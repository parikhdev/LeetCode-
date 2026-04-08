from functools import reduce
from operator import xor

def xorAfterQueries(nums, queries):
    mod = 10**9 + 7
    for l, r, k, v in queries:
        for idx in range(l, r + 1, k):
            nums[idx] = nums[idx] * v % mod
    return reduce(xor, nums)

print(xorAfterQueries([1,1,1],[[0,2,1,4]]))