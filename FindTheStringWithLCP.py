def findTheString(lcp):
    n = len(lcp)
    s = ['?'] * n
    c = 0

    for i in range(n):
        if s[i] != '?':
            continue
        if c >= 26:
            return ""
        for j in range(i, n):
            if lcp[i][j] > 0:
                s[j] = chr(ord('a') + c)
        c += 1

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            expected = 0
            if s[i] == s[j]:
                expected = 1 + (lcp[i+1][j+1] if i+1 < n and j+1 < n else 0)
            if lcp[i][j] != expected:
                return ""

    return "".join(s)
print(findTheString([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]))