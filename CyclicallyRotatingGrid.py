def rotateGrid(grid, k):
    m, n = len(grid), len(grid[0])
    for layer in range(min(m, n) // 2):
        r1, c1, r2, c2 = layer, layer, m - 1 - layer, n - 1 - layer
        coords = []
        for r in range(r1, r2): coords.append((r, c1))
        for c in range(c1, c2): coords.append((r2, c))
        for r in range(r2, r1, -1): coords.append((r, c2))
        for c in range(c2, c1, -1): coords.append((r1, c))
        
        vals = [grid[r][c] for r, c in coords]
        k_eff = k % len(vals)
        rotated = vals[-k_eff:] + vals[:-k_eff]
        
        for i, (r, c) in enumerate(coords):
            grid[r][c] = rotated[i]
    return grid

print(rotateGrid([[40,10],[30,20]], 1))