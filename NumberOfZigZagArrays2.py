def zigZagArrays(n, l, r):
    MOD = 10**9 + 7
    m = r - l + 1
    states = 2 * m
    
    def multiply(A, B):
        C = [[0] * states for _ in range(states)]
        for i in range(states):
            for k in range(states):
                if A[i][k]:
                    for j in range(states):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
        return C

    def power(base, exp):
        res = [[0] * states for _ in range(states)]
        for i in range(states):
            res[i][i] = 1
        while exp > 0:
            if exp % 2 == 1:
                res = multiply(res, base)
            base = multiply(base, base)
            exp //= 2
        return res

    T = [[0] * states for _ in range(states)]
    for x in range(m):
        down = x
        up = x + m
        for y in range(x + 1, m):
            T[y][up] = 1
        for y in range(x):
            T[y + m][down] = 1
            
    P = power(T, n - 1)
    
    ans = 0
    for row in P:
        ans = (ans + sum(row)) % MOD
        
    return ans

print(zigZagArrays(3,4,5))