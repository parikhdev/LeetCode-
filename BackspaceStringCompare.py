def build(s):
    stack = []
    for ch in s:
        if ch == '#':
            if stack:
                stack.pop()
        else:
            stack.append(ch)
    return stack

def backspaceCompare(s, t):
    return build(s) == build(t)
print(backspaceCompare("a#bbb", "c#bbb"))
