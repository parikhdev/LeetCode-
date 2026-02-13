def maxTurbulenceSize(arr):
    n = len(arr)
    if n == 1:
        return 1
    prev_Sign = 0
    curr_len = 1
    Max_len = 1
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            sign = 1
        elif arr[i] < arr[i-1]:
            sign = -1
        else:
            sign = 0
        
        if sign == 0:
            curr_len = 1
        elif sign == -prev_Sign:
            curr_len += 1
        else:
            curr_len = 2
        Max_len = max(Max_len, curr_len)
        prev_Sign = sign
    return Max_len
print(maxTurbulenceSize([1,3,2,5,4,7,6,9,8]))

