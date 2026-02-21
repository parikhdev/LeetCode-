from operator import itemgetter
def frequencySort(s):
    SortDict = {}
    res = ""
    for num in s:
        SortDict[num] = SortDict.get(num,0) + 1
    Arr = sorted(SortDict.items(),key= itemgetter(1), reverse = True)
    for char, freq in Arr:
        res += char*freq
    return res
print(frequencySort("ssaaat"))
