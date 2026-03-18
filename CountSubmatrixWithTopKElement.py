def countSubmatrices(grid,k):
    rows = len(grid)
    cols = len(grid[0])
    max_c = cols
    count = 0
    for r in range(rows):
        for c in range(max_c):
            if r > 0:
                grid[r][c] += grid[r-1][c]
            if c > 0:
                grid[r][c] += grid[r][c-1]
            if r > 0 and c > 0:
                grid[r][c] -= grid[r-1][c-1]
            if grid[r][c] <= k:
                count += 1
            else:
                max_c = c
                break
    return count
print(countSubmatrices([[7,6,3],[6,6,1]],18))


