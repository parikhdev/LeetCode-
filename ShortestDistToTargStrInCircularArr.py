def closestTarget(words, target, startIndex):
    n = len(words)
    ans = n
    for i in range(n):
        if words[i] == target:
            diff = abs(i - startIndex)
            ans = min(ans, diff, n- diff)
    return ans if ans != n else -1

print(closestTarget(["hello","i","am","leetcode","hello"],  "hello", 1))