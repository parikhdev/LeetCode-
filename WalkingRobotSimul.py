def robotSim(commands, obstacles):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x = y = di = 0
    obstacle_Set = set(map(tuple,obstacles))
    max_sq_distance = 0

    for i in commands:
        if i == -2:
            di = (di - 1) % 4
        elif i == -1:  
            di = (di + 1) % 4
        else:  
            for _ in range(i):
                next_x = x + dx[di]
                next_y = y + dy[di]
            
                if (next_x, next_y) not in obstacle_Set:
                    x, y = next_x, next_y
                    max_sq_distance = max(max_sq_distance, x*x + y*y)
                else:
                    break
                    
    return max_sq_distance
print(robotSim([4,-1,3], []))
        