
def rotate(matrix):
    
    n = len(matrix)
    
    # Tranpose
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reflection
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
new = [[1,2,3],[4,5,6],[7,8,9]]
rotate(new)
print(new)