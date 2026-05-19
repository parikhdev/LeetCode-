def getCommon(nums1, nums2): 
    common = set(nums1) & set(nums2)
    return min(common) if common else -1

print(getCommon([1,2,3],[2,4]))