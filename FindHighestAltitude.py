def largestAltitude(gain):
        altitude = [0]
        currSum = 0
        for i, num in enumerate(gain):
            currSum += num
            altitude.append(currSum)
        return max(altitude)

print(largestAltitude([1,-4,5,-7,2]))