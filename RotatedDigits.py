def rotatedDigits(n): 
    count = 0
    
    for i in range(1, n + 1):
        s = str(i)
        if '3' in s or '4' in s or '7' in s:
            continue
        if any(d in s for d in '2569'):
            count += 1
            
    return count
print(rotatedDigits(10))