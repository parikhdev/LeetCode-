def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration): 
    def get_time(start1, dur1, start2, dur2):
        first_finish = float('inf')
        for s, d in zip(start1, dur1):
            first_finish = min(first_finish, s + d)
            
        total_finish = float('inf')
        for s, d in zip(start2, dur2):
            total_finish = min(total_finish, max(first_finish, s) + d)
            
        return total_finish

    return min(
        get_time(landStartTime, landDuration, waterStartTime, waterDuration),
        get_time(waterStartTime, waterDuration, landStartTime, landDuration)
    )
print(earliestFinishTime([2,8],[4,1],[6],[3]))