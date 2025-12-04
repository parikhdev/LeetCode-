def inttostr(i):
    digits = "0123456789"
    if i == 0:
        return '0'
    box = ''
    while i > 0:
        box = digits[i%10] + box 
        i = i//10
    print(type(box))
    return box

print(inttostr(890))


