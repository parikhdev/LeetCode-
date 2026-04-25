from typing import List

def maxDistance(side, points, k):
    def get_pos(p):
        x, y = p
        if y == 0: return x
        if x == side: return side + y
        if y == side: return 3 * side - x
        return 4 * side - y

    points.sort(key=get_pos)
    n = len(points)
    pts = [tuple(p) for p in points]
    pts2 = pts + pts
    
    def check(d):
        nxt = [0] * (2 * n)
        r = 0
        for i in range(2 * n):
            if r <= i: r = i + 1
            xi, yi = pts2[i]
            while r < 2 * n:
                xr, yr = pts2[r]
                if abs(xi - xr) + abs(yi - yr) >= d:
                    break
                r += 1
            nxt[i] = r
        
        for i in range(n):
            curr = i
            for _ in range(k - 1):
                curr = nxt[curr]
                if curr >= i + n:
                    break
            else:
                xi, yi = pts2[i]
                xc, yc = pts2[curr]
                if abs(xi - xc) + abs(yi - yc) >= d:
                    return True
        return False

    low, high = 0, 2 * side
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

print(maxDistance(2,[[0,2],[2,0],[2,2],[0,0]], 4))