from collections import Counter
def maximumLength(nums): 
        freq = Counter(nums)
        ans = 1
        
        if 1 in freq:
            ans = freq[1] if freq[1] % 2 == 1 else freq[1] - 1
            
        for k in freq:
            if k == 1:
                continue
                
            curr = k
            count = 0
            
            while freq[curr] > 1:
                count += 2
                curr *= curr
                
            if freq[curr] > 0:
                count += 1
            else:
                count -= 1
                
            if count > ans:
                ans = count
                
        return ans
print(maximumLength([5,4,1,2,2]))