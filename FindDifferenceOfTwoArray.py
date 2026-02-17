def findDifference(nums1,nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    list1 = list(set1 - set2)
    list2 = list(set2 - set1)
    return [list1,list2]
print(findDifference([2,1,4,5],[3,2,4,6]))