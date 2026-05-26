def numberOfSpecialChars(word): 
    seen = set(word)
    count = 0
    
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c in seen and c.upper() in seen:
            count += 1
            
    return count

print(numberOfSpecialChars("aaAbcBC"))