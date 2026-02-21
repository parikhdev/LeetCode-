import math
def countPrimeSetBits(left,right):
    def Prime(a):
        if a <= 1:
            return False
        elif a == 2:
            return True
        elif a % 2 == 0:
            return False
        limit = int(math.sqrt(a)) + 1
        for i in range(3,limit,2):
            if a % i == 0:
                return False
        return True
    count = 0
    for i in range(left, right+1):
        set_bits = i.bit_count()
        if Prime(set_bits) == True:
            count += 1
    return count
print(countPrimeSetBits(6,10))