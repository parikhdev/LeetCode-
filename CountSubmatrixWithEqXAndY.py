def numberOfSubmatrices(grid):
    m, n = len(grid), len(grid[0])
    s = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
    ans = 0
    for i, row in enumerate(grid, 1):
        for j, cell in enumerate(row, 1):
            s[i][j][0] = s[i-1][j][0] + s[i][j-1][0] - s[i-1][j-1][0]
            s[i][j][1] = s[i-1][j][1] + s[i][j-1][1] - s[i-1][j-1][1]
            if cell == 'X':
                s[i][j][0] += 1
            elif cell == 'Y':
                s[i][j][1] += 1
            if s[i][j][0] > 0 and s[i][j][0] == s[i][j][1]:
                ans += 1
    return ans
print(numberOfSubmatrices([["X","Y","."],["Y",".","."]]))