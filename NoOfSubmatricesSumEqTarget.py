import collections
def numSubmatrixSumTarget(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    ans = 0

    for row in matrix:
      for i in range(1, n):
        row[i] += row[i - 1]

    for baseCol in range(n):
      for j in range(baseCol, n):
        prefixCount = collections.Counter({0: 1})
        summ = 0
        for i in range(m):
          if baseCol > 0:
            summ -= matrix[i][baseCol - 1]
          summ += matrix[i][j]
          ans += prefixCount[summ - target]
          prefixCount[summ] += 1

    return ans
print(numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0))