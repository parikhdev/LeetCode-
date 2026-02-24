from collections import Counter
def commonChars(words):
    common = Counter(words[0])
    for i in range(1, len(words)):
        common &= Counter(words[i])
    return list(common.elements())
print(commonChars(["bella", "mella", "thella"]))
