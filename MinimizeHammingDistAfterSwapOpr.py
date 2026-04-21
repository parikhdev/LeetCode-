from collections import Counter, defaultdict
def minimumHammingDistance(source, target, allowedSwaps): 
    n = len(source)
    parent = list(range(n))

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i]) 
        return parent[i]

    for u, v in allowedSwaps:
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v

    components = defaultdict(Counter)
    for i in range(n):
        components[find(i)][source[i]] += 1
        
    hamming_dist = 0
    for i in range(n):
        root = find(i)
        val = target[i]
        if components[root][val] > 0:
            components[root][val] -= 1
        else:
            hamming_dist += 1
            
    return hamming_dist

print(minimumHammingDistance([1,2,3,4],[2,1,4,5],[[0,1],[2,3]]))