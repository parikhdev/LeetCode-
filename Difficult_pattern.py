#Diamond
# n = 5
# p = 65
# for i in range(n-1):
#     # p = 65
#     for j in range(i, n):
#         print(" ", end = " ")
#     for j in range(i):
#         print(chr(p), end = " ")
#         # p += 1
#     for j in range(i+1):
#         print(chr(p), end = " ")
#     p += 1
#     print()
# p = 65
# for i in range(n):
#     # p = 65
#     for j in range(i+1):
#         print(" ", end = " ")
#     for j in range(i, n-1):
#         print(chr(p), end = " ")
#         # p += 1
#     for j in range(i, n):
#         print(chr(p), end = " ")
#     p += 1
#     print()

# Butterfly
s = 'SUPER'
n = len(s)
for i in range(n-1):
    p = 0
    q = n-1
    for j in range(i+1):
        print(s[p], end = " ")
        p += 1
    for j in range(i,n-1):
        print(" ", end = " ")
    for j in range(i, n-1):
        print(" ", end = " ")
    for j in range(i+1):
        print(s[q], end = " ")
        q -= 1
    print()
for i in range(n):
    p = 0
    q = n-1
    for j in range(i, n):
        print(s[p], end = " ")
        p += 1
    for j in range(i):
        print(" ", end = " ")
    for j in range(i):
        print(" ", end = " ")
    for j in range(i, n):
        print(s[q], end = " ")
        q -= 1
    print()