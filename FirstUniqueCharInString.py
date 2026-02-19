def firstUniqChar(s):
    map1 = {}
    for ch in s:
        map1[ch] = map1.get(ch,0) + 1
    for i, ch in enumerate(s):
        if map1[ch] == 1:
            return i
    return -1
print(firstUniqChar("MorePlumSauceMore"))
        