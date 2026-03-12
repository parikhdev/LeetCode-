def strStr(haystack,needle):
    n = len(haystack)
    window = len(needle)
    if window > n:
        return -1
    for i in range(n - window + 1):
        if haystack[i:i+window] == needle:
            return i
    return -1
print(strStr("IAmAChillKindAGuy", "Chill"))

        