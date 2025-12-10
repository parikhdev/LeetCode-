def findAnagrams(s, p):
    if len(p) > len(s): return []
    p_count = [0] * 26
    s_count = [0] * 26
    result = []
    def get_index(char):
        return ord(char) - ord('a')
    for i in range(len(p)):
        p_count[get_index(p[i])] += 1
        s_count[get_index(s[i])] += 1
    if s_count == p_count:
        result.append(0)
    l = 0
    for r in range(len(p), len(s)):
        s_count[get_index(s[r])] += 1
        s_count[get_index(s[l])] -= 1
        l += 1
        if s_count == p_count:
            result.append(l)      
    return result

print(findAnagrams("cbaebabacd", "abc"))