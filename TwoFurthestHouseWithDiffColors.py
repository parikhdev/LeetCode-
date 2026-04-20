def maxDistance(colors):
    n = len(colors)
    HighestDistance = 0
    for diff in range(n-1,0,-1):
        if colors[0] != colors[diff]:
            HighestDistance = max(HighestDistance, diff)
            break

    for diff in range(n-1):
        if colors[n-1] != colors[diff]:
            HighestDistance = max(HighestDistance, n-1-diff)
            break
    return HighestDistance

print(maxDistance([4,4,4,11,4,4,11,4,4,4,4,4]))