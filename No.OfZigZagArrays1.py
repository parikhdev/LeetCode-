def zigZagArrays(n, l, r): 
    MOD = 10**9 + 7
    r -= l
    dp = [1] * (r + 1)
    
    for i in range(1, n):
        pre = 0
        if i % 2 == 1:
            for v in range(r + 1):
                pre2 = (pre + dp[v]) % MOD
                dp[v] = pre
                pre = pre2
        else:
            for v in range(r, -1, -1):
                pre2 = (pre + dp[v]) % MOD
                dp[v] = pre
                pre = pre2
                
    return (sum(dp) * 2) % MOD

print(zigZagArrays(3,4,5))