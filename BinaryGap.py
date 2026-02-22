def binaryGap(n):
    a = bin(n)[2:]
    maxgap = 0
    left = -1
    for i, ch in enumerate(a):
        if ch == '1':
            if left != -1:
                maxgap = max(maxgap, i - left)
            left = i
    return maxgap
print(binaryGap(16))   

    