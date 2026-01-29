def corpFlightBookings(bookings, n):
        diff = [0] * n
        for booking in bookings:
            start, end, seats = booking
            diff[start - 1] += seats
            if end < n:
                diff[end] -= seats
        for i in range(1, n):
            diff[i] += diff[i - 1]
        return diff
print(corpFlightBookings([[1,2,10], [2,3,40]],3))
