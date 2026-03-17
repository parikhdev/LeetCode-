def largestSubmatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1, rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                matrix[i][j] += matrix[i-1][j]
    max_area = 0

    for row in matrix:
        row.sort(reverse=True)
        for j in range(cols):
            area = row[j] * (j + 1)
            max_area = max(max_area, area)
    return max_area
print(largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))