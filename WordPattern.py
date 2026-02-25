def wordPattern(pattern ,s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))
print(wordPattern("abba", "word more more word"))