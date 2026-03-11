def compress(chars):
    left = 0
    right = 0
    n = len(chars)
    while right < n:
        start = right
        while right < n and chars[right] == chars[start]:
            right += 1
        chars[left] = chars[start]
        left += 1
        count = right - start
        if count > 1:
            for c in str(count):
                chars[left] = c
                left += 1
    return left
print(compress(['a','b','c','d','d']))
