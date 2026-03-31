def generateString(str1, str2):
    n, m = len(str1), len(str2)
    ans = ['?'] * (n + m - 1)

    for i in range(n):
        if str1[i] == 'T':
            for j in range(m):
                if ans[i + j] == '?' or ans[i + j] == str2[j]:
                    ans[i + j] = str2[j]
                else:
                    return ""

    for i in range(len(ans)):
        if ans[i] == '?':
            ans[i] = 'a'

    def valid_T_local(ans, idx):
        for k in range(max(0, idx - m + 1), min(n, idx + 1)):
            if str1[k] == 'T':
                if ''.join(ans[k:k+m]) != str2:
                    return False
        return True

    for i in range(n):
        if str1[i] == 'F':
            if ''.join(ans[i:i+m]) == str2:
                for j in reversed(range(m)):
                    idx = i + j
                    original = ans[idx]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != original:
                            ans[idx] = c
                            if ''.join(ans[i:i+m]) != str2 and valid_T_local(ans, idx):
                                break
                            ans[idx] = original
                    else:
                        continue
                    break
                else:
                    return ""

    return ''.join(ans)

print(generateString("TFTF", "ab"))