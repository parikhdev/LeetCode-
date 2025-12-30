class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def height(node):
            nonlocal diameter
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        height(root)
        return diameter
def buildTree(arr):
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(x) for x in arr]
    for i in range(len(arr)):
        if nodes[i]:
            if 2*i+1 < len(arr): nodes[i].left = nodes[2*i+1]
            if 2*i+2 < len(arr): nodes[i].right = nodes[2*i+2]
    return nodes[0]
root_list = [1, 2, 3, 4, 5]
root = buildTree(root_list)
print(f"Input: root = {root_list}")
print("Output:", Solution().diameterOfBinaryTree(root))
