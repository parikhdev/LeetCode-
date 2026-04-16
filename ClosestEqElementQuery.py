from collections import defaultdict

def solveQueries(nums, queries):
    n = len(nums)
    pos_map = defaultdict(list)
    for i, val in enumerate(nums):
        pos_map[val].append(i)
    min_distances = [-1] * n
    
    for val, indices in pos_map.items():
        m = len(indices)
        if m < 2:
            continue
        
        for i in range(m):
            curr_idx = indices[i]
            prev_idx = indices[i - 1]
            dist_prev = (curr_idx - prev_idx) % n
            next_idx = indices[(i + 1) % m]
            dist_next = (next_idx - curr_idx) % n
            min_distances[curr_idx] = min(dist_prev, dist_next)
        
    return [min_distances[q] for q in queries]

print(solveQueries([1,3,1,4,1,3,2],[0,3,5]))