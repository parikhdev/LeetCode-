def numJewelsInStones(jewels,stones):
    jewelset = set(jewels)
    count = 0
    for stone in stones:
        if stone in jewelset:
            count += 1
    return count
print(numJewelsInStones("aZ", "abcdefyZ"))