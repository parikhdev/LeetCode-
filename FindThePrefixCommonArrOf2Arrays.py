def findThePrefixCommonArray(A,B): 
    n = len(A)
    C = [0] * n
    seen = [0] * (n + 1)
    common_count = 0
    for i in range(n):
        seen[A[i]] += 1
        if seen[A[i]] == 2:
            common_count += 1
        seen[B[i]] += 1
        if seen[B[i]] == 2:
            common_count += 1
        C[i] = common_count
    return C
print(findThePrefixCommonArray([1,3,2,4],[3,1,2,4]))