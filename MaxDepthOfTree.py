class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
def buildTree(arr):
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(x) for x in arr]
    for i in range(len(arr)):
        if nodes[i]:
            l, r = 2*i+1, 2*i+2
            if l < len(arr): nodes[i].left = nodes[l]
            if r < len(arr): nodes[i].right = nodes[r]
    return nodes[0]
root_list = [3, 9, 20, None, None, 15, 7]

root = buildTree(root_list)
print(f"Input: root = {root_list}")
print("Output:", Solution().maxDepth(root))
