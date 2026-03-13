def compareVersion(version1,version2):
    a = version1.split('.')
    b = version2.split('.')
    maxlen = max(len(a), len(b))
    for i in range(maxlen):
        v1 = int(a[i]) if i < len(a) else 0
        v2 = int(b[i]) if i < len(b) else 0
        if v1 < v2:
            return -1 
        elif v1 > v2:
            return 1
    return 0
print(compareVersion('1.1.2', '1.2.0'))