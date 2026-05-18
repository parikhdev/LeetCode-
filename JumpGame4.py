from collections import deque, defaultdict

def minJumps(arr): 
    n = len(arr)
    if n <= 1:
        return 0
    
    graph = defaultdict(list)
    for i, val in enumerate(arr):
        graph[val].append(i)
        
    queue = deque([(0, 0)])
    visited = {0}
    
    while queue:
        idx, steps = queue.popleft()
        
        if idx == n - 1:
            return steps
        
        neighbors = [idx - 1, idx + 1] + graph[arr[idx]]
        graph[arr[idx]] = []
        
        for nxt in neighbors:
            if 0 <= nxt < n and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, steps + 1))        
    return -1

print(minJumps([100,-23,-23,404,100,23,23,23,3,404]))