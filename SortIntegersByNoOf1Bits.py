def sortByBits(arr):
    def count_ones(n):
        count = 0
        while n > 0:
            n &= (n - 1) 
            count += 1
        return count
    return sorted(arr, key=lambda x: (count_ones(x), x))
print(sortByBits([0,1,2,3,4,5,6,7,8]))
        