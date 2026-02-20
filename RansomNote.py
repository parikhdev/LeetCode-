def canConstruct(ransomNote, magazine):
    if len(ransomNote) > len(magazine):
        return False
    map1 = {}
    for i in range(len(magazine)):
        map1[magazine[i]] = map1.get(magazine[i], 0) + 1
    for num in ransomNote:
        if map1.get(num,0) > 0:
            map1[num] = map1.get(num, 0) - 1
        else:
            return False
    return True
print(canConstruct("aa", "aaa"))