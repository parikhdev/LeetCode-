from typing import List

def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration): 
    def calc(start1, dur1, start2, dur2):
        min_end = min(s + d for s, d in zip(start1, dur1))
        return min(max(s, min_end) + d for s, d in zip(start2, dur2))
        
    return min(
        calc(landStartTime, landDuration, waterStartTime, waterDuration),
        calc(waterStartTime, waterDuration, landStartTime, landDuration)
    )

print(earliestFinishTime([2,8],[4,1],[6],[3]))