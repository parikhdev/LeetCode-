def numberOfSpecialChars(word): 
    states = [0] * 26
    
    for char in word:
        idx = ord(char.lower()) - 97
        if char.islower():
            if states[idx] == 0 or states[idx] == 1:
                states[idx] = 1
            elif states[idx] == 2:
                states[idx] = -1
        else:
            if states[idx] == 1 or states[idx] == 2:
                states[idx] = 2
            elif states[idx] == 0:
                states[idx] = -1    
    return sum(1 for state in states if state == 2)

print(numberOfSpecialChars("aaAbcBC"))