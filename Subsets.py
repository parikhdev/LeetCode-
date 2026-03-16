def subsets(nums):
    def dfs(i, path):
        res.append(path[:])
        for j in range(i, len(nums)):
            path.append(nums[j])
            dfs(j + 1, path)
            path.pop()
    res = []
    dfs(0,[])
    print(res)
    return res
subsets([1,2,3])



                