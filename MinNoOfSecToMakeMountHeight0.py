from typing import List
import math


def minNumberOfSeconds(mountainHeight, workerTimes):

    def can(T):
        total = 0
        for t in workerTimes:
            k = int((math.sqrt(1 + 8*T/t) - 1) // 2)
            total += k
            if total >= mountainHeight:
                return True
        return False

    left, right = 0, 10**18

    while left < right:
        mid = (left + right) // 2
        if can(mid):
            right = mid
        else:
            left = mid + 1

    return left
print(minNumberOfSeconds(4, [1,2,3]))