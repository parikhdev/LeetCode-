def reverseWords(s):
    List = s.split()[::-1]
    n = len(List)
    return " ".join(List)
print(reverseWords("The strip is black"))
    