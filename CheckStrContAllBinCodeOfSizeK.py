def hasAllCodes(s,k):
    needed = 1 << k
    got = set()
    for i in range(len(s) - k + 1):
        tmp = s[i:i+k]
        if tmp not in got:
            got.add(tmp)
            needed -= 1
        if needed == 0:
            return True
    return False
print(hasAllCodes("00110110",2))
