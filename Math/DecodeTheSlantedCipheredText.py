def decodeCiphertext(encodedText, rows):
    cols = len(encodedText)//rows
    original = []
    for c in range(cols):
        r = 0
        while r < rows and c < cols:
            original.append(encodedText[cols * r + c])
            r += 1
            c += 1
    return ''.join(original).rstrip()

print(decodeCiphertext("ch   ie   pr", 3))
