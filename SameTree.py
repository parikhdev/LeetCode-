class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
def buildTree(arr):
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(x) for x in arr]
    for i in range(len(arr)):
        if nodes[i]:
            if 2*i+1 < len(arr): nodes[i].left = nodes[2*i+1]
            if 2*i+2 < len(arr): nodes[i].right = nodes[2*i+2]
    return nodes[0]
p_list = [1, 2, 3]
q_list = [1, 2, 3]

p = buildTree(p_list)
q = buildTree(q_list)

print(f"Input: p = {p_list}, q = {q_list}")
print("Output:", Solution().isSameTree(p, q))
