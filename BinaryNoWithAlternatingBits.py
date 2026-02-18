def hasAlternatingBits(n):
    x = n ^ (n >> 1)
    return (x & (x+1)) == 0
print(hasAlternatingBits(10))