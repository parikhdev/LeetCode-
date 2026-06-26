def countMajoritySubarrays(nums, target):
        n = len(nums)
        bit = [0] * (2 * n + 2)
        
        def add(idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        ans = 0
        curr = n + 1
        add(curr, 1)
        
        for num in nums:
            curr += 1 if num == target else -1
            ans += query(curr - 1)
            add(curr, 1)
            
        return ans

print(countMajoritySubarrays([1,2,2,3], 2))