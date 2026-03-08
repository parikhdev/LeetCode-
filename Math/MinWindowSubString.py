def minWindow(s,t):
    if len(t) > len(s):
        return ""
    freq = {}
    window = {}
    for i in t:
        freq[i] = freq.get(i, 0) + 1
    have = 0
    need = len(freq)
    res = [-1, -1]
    res_len = float("inf")
    l = 0

    for r in range(len(s)):
        window[s[r]] = window.get(s[r], 0) + 1

        if s[r] in freq and window[s[r]] == freq[s[r]]:
            have += 1

        while have == need:

            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1

            window[s[l]] -= 1
            if s[l] in freq and window[s[l]] < freq[s[l]]:
                have -= 1

            l += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""
print(minWindow("ABCDE", "CDE"))
    