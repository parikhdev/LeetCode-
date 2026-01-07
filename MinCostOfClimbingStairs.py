def minCostClimbingStairs(cost):
    prev = curr = 0
    for i in range(2, len(cost) + 1):
        prev, curr = curr, min(cost[i-2] + prev, cost[i-1] + curr)
    return curr
cost = [1,100,1,1,1,100,1,1,100,1]
print(f"Input: cost = {cost}")
print("Output:", minCostClimbingStairs(cost))