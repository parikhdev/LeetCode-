def longestNiceSubstring(s):
    if len(s) < 2:
        return ""
    char_set = set(s)
    for i, c in enumerate(s):
        if c.swapcase() not in char_set:
            left = longestNiceSubstring(s[:i])
            right = longestNiceSubstring(s[i+1:])
            return left if len(left) >= len(right) else right
    return s
print(longestNiceSubstring("YazaAay"))