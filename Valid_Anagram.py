# Approach 1
# def isAnagram(s, t):
#     s = s.lower()
#     t = t.lower()
#     if len(s) != len(t):
#         return False
#     sorted_s = "".join(sorted(s))
#     sorted_t = "".join(sorted(t))
#     if sorted_s == sorted_t:
#         return True
#     else:
#         return False 

# print(isAnagram("Anagram", "Nagaram"))
# print(isAnagram("Cat", "Rat"))

# Approach 2
def isAnagram(s, t):
    s = s.lower()
    t = t.lower()
    if len(s) != len(t):
        return False
    dict = {}
    for char in s:
        dict[char] = dict.get(char,0) + 1
    for char in t:
        if char not in dict:
            return False
        dict[char] -= 1
    return True

print(isAnagram("Anagram", "Nagaram"))
print(isAnagram("Cat", "Rat"))