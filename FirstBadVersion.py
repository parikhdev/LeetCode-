def isBadVersion(version):
    first_bad_version = 7
    return version >= first_bad_version

def firstBadVersion(n):
    L = 1
    R = n
    while L < R:
        M = (L+R) // 2
        if isBadVersion(M):
            R = M
        else:
            L = M + 1
    return L 
        
print(firstBadVersion(9))