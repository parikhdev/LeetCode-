from collections import Counter

def findSubstring(s,words):
    if not s or not words:
        return []
    word_len = len(words[0])
    word_count = Counter(words)
    total_words = len(words)
    result = []
    for i in range(word_len):
        left = i
        window = {}
        count = 0
        for right in range(i, len(s) - word_len + 1, word_len):
            word = s[right:right + word_len]
            if word in word_count:
                window[word] = window.get(word, 0) + 1
                count += 1
                while window[word] > word_count[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1
                if count == total_words:
                    result.append(left)
            else:
                window.clear()
                count = 0
                left = right + word_len
    return result
print(findSubstring("coolheroboydoomherocool", ["cool", "hero"]))