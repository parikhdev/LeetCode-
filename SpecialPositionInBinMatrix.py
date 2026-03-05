from typing import List

def numSpecial(mat):
    m = len(mat)
    n = len(mat[0])
    
    row_count = [0] * m
    col_count = [0] * n

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                row_count[i] += 1
                col_count[j] += 1
                
    special_count = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                special_count += 1
                
    return special_count
        
print(numSpecial([[1,0,0],[0,0,1],[1,0,0]]))