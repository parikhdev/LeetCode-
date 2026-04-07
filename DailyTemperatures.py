def dailyTemperatures(temperatures): 
    n = len(temperatures)
    Res = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            lowerTempIdx = stack.pop()
            Res[lowerTempIdx] = i - lowerTempIdx
        if i < n:
            stack.append(i)
    return Res
print(dailyTemperatures([73,74,75,71,69,72,76,73]))
