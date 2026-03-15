def removeDuplicates(s):
    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)
print(removeDuplicates("abbaYP"))