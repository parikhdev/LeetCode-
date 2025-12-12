def lengthOfLongestSubstring(s):
    l = 0
    longest = 0
    box = set()
    n = len(s)
    for r in range(n):
        while s[r] in box:
            box.remove(s[l])
            l += 1
        w = (r - l) + 1
        longest = max(longest, w)
        box.add(s[r])
    return longest
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbb"))