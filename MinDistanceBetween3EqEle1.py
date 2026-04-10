from collections import defaultdict
def minimumDistance(nums):
    index_map = defaultdict(list)
    for idx, val in enumerate(nums):
        index_map[val].append(idx)
    
    min_dist = float('inf')
    
    for index in index_map.values():
        if len(index) < 3:
            continue
        for i in range(len(index) - 2):
            current_dist = 2 * (index[i + 2] - index[i])
            if current_dist < min_dist:
                min_dist = current_dist
    
    return min_dist if min_dist != float('inf') else -1

print(minimumDistance([1,2,1,1,3]))