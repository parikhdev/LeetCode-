from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)

        return res
def buildTree(arr):
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(x) for x in arr]
    for i in range(len(arr)):
        if nodes[i]:
            if 2*i+1 < len(arr): nodes[i].left = nodes[2*i+1]
            if 2*i+2 < len(arr): nodes[i].right = nodes[2*i+2]
    return nodes[0]
root_list = [3, 9, 20, None, None, 15, 7]
root = buildTree(root_list)
print(f"Input: root = {root_list}")
print("Output:", Solution().levelOrder(root))
