def makeLargestSpecial(s) -> str:
    count = 0
    i = 0
    res = []
    for j, char in enumerate(s):
        count += 1 if char == '1' else -1
        if count == 0:
            inner_solved = makeLargestSpecial(s[i + 1:j])
            res.append("1" + inner_solved + "0")
            i = j + 1
    res.sort(reverse=True)
    return "".join(res)
print(makeLargestSpecial("11011000"))