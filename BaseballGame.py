def calPoints(operations):
    stack = []
    for i in operations:
        if i == 'C':
            stack.pop()
        elif i == 'D':
            stack.append(stack[-1] * 2)
        elif i == '+':
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(i))
    return sum(stack)
print(calPoints(["5","2","C","D","+"]))
