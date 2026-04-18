def mirrorDistance(n):
    return abs(n - int(str(n)[::-1]))

print(mirrorDistance(25))