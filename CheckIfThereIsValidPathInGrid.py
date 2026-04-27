from collections import deque

def hasValidPath(grid):
    rows, cols = len(grid), len(grid[0])
    directions = {
        1: [(0, -1), (0, 1)],
        2: [(-1, 0), (1, 0)],
        3: [(0, -1), (1, 0)],
        4: [(0, 1), (1, 0)],
        5: [(0, -1), (-1, 0)],
        6: [(0, 1), (-1, 0)]
    }
    
    queue = deque([(0, 0)])
    visited = {(0, 0)}
    
    while queue:
        r, c = queue.popleft()
        
        if r == rows - 1 and c == cols - 1:
            return True
        
        for dr, dc in directions[grid[r][c]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if (-dr, -dc) in directions[grid[nr][nc]]:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
    
    return False

print(hasValidPath([[2,4,3],[6,5,2]]))