def minimumCost(cost): 
    cost.sort(reverse=True)
    total = 0
    
    for i, price in enumerate(cost):
        if i % 3 != 2:
            total += price    
    return total
print(minimumCost([1,2,3]))