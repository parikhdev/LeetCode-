class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
def buildTree(arr):
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(x) for x in arr]
    for i in range(len(arr)):
        if nodes[i]:
            if 2*i+1 < len(arr): nodes[i].left = nodes[2*i+1]
            if 2*i+2 < len(arr): nodes[i].right = nodes[2*i+2]
    return nodes[0]
def treeToList(root):
    if not root:
        return []
    res, q = [], [root]
    while q:
        node = q.pop(0)
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res
root_list = [4, 2, 7, 1, 3, 6, 9]

root = buildTree(root_list)
inverted = Solution().invertTree(root)

print(f"Input: root = {root_list}")
print("Output:", treeToList(inverted))
