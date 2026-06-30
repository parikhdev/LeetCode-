def numberOfSubstrings(s):
    ans = 0
    last = {'a': -1, 'b': -1, 'c': -1}
    
    for i, c in enumerate(s):
        last[c] = i
        ans += min(last['a'], last['b'], last['c']) + 1
        
    return ans

print(numberOfSubstrings("abcabc"))