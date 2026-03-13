def licenseKeyFormatting(s,k):
    a = s.replace('-', '').upper()
    res = []
    firstLen = len(a) % k 
    if firstLen > 0:
        res.append(a[:firstLen])
    for i in range(firstLen, len(a), k):
        res.append(a[i:i+k])
    return '-'.join(res)
print(licenseKeyFormatting('abd-gh-09-0k', 3))