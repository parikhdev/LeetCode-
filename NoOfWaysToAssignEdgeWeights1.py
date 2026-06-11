from typing import List
from collections import deque

def assignEdgeWeights(edges):
    if not edges:
        return 0
        
    n = len(edges) + 1
    graph = [[] for _ in range(n + 1)]
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    max_depth = 0
    queue = deque([(1, -1, 0)])
    
    while queue:
        node, parent, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        
        for neighbor in graph[node]:
            if neighbor != parent:
                queue.append((neighbor, node, depth + 1))
                
    return pow(2, max_depth - 1, 10**9 + 7)

print(assignEdgeWeights([[1,2]]))