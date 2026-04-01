def survivedRobotsHealths(positions, healths, directions):
    n = len(positions)
    
    indices = sorted(range(n), key=lambda i: positions[i])
    stack = [] 
    
    for i in indices:
        if directions[i] == 'R':
            stack.append(i)
        else:
            while stack and healths[i] > 0:
                top = stack[-1]
                
                if healths[top] > healths[i]:       
                    healths[top] -= 1
                    healths[i] = 0
                elif healths[top] < healths[i]:    
                    healths[i] -= 1
                    healths[top] = 0
                    stack.pop()
                else:                               
                    healths[i] = 0
                    healths[top] = 0
                    stack.pop()
    
    return [healths[i] for i in range(n) if healths[i] > 0]

print(survivedRobotsHealths([3,5,2,6],[10,10,15,12],"RLRL"))

        