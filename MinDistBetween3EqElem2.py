from typing import List
from collections import defaultdict

def minimumDistance(nums):
    indices = defaultdict(list)
    for i, num in enumerate(nums):
        indices[num].append(i)
    
    ans = float('inf')
    for pos in indices.values():
        if len(pos) >= 3:
            for i in range(len(pos) - 2):
                ans = min(ans, 2 * (pos[i + 2] - pos[i]))
    
    return int(ans) if ans != float('inf') else -1

print(minimumDistance([1,2,1,1,3]))