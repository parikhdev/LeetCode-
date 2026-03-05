def minOperations(s):
    count0 = 0 
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != '0':
                count0 += 1
        else:
            if s[i] != '1':
                count0 += 1
    return min(count0, len(s) - count0)
print(minOperations("010100"))