from bisect import bisect_left, bisect_right
from math import inf

def maxWalls(robots, distance, walls):
    
    def count(v, x, y):
        return bisect_right(v, y) - bisect_left(v, x) if x <= y else 0
    
    p = sorted(zip(robots, distance))
    walls.sort()
    n = len(p)
    left_num = right_num = 0
    
    for i, (pos, dist) in enumerate(p):
        prev_pos = p[i-1][0] if i > 0 else 0
        prev_end = p[i-1][0] + p[i-1][1] if i > 0 else 0
        next_pos = p[i+1][0] if i+1 < n else inf
        
        n_left = max(
            count(walls, max(prev_pos + 1, pos - dist), pos) + left_num,
            count(walls, max(prev_end + 1, pos - dist), pos) + right_num
        )
        n_right = count(walls, pos, min(pos + dist, next_pos - 1)) + max(left_num, right_num)
        
        left_num, right_num = n_left, n_right
    
    return max(left_num, right_num)

print(maxWalls([4], [3], [1,10]))