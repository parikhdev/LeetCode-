def intersection(nums1, nums2):
    ans = []
    nums1 = set(nums1)
    for num in nums2:
      if num in nums1:
        ans.append(num)
        nums1.remove(num)
    return ans

print(intersection([1,2,3,4,5],[4,3,6]))
    