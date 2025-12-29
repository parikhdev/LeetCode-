class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
class Solution:
    def isSubtree(self, root, subRoot):
        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def hasSubtree(node):
            if not node:
                return False
            if sameTree(node, subRoot):
                return True
            return hasSubtree(node.left) or hasSubtree(node.right)

        return hasSubtree(root)
def buildTree(arr):
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(x) for x in arr]
    for i in range(len(arr)):
        if nodes[i]:
            if 2*i+1 < len(arr): nodes[i].left = nodes[2*i+1]
            if 2*i+2 < len(arr): nodes[i].right = nodes[2*i+2]
    return nodes[0]
# -------- Input --------
root_list = [3, 4, 5, 1, 2]
subroot_list = [4, 1, 2]

root = buildTree(root_list)
subRoot = buildTree(subroot_list)

print(f"Input: root = {root_list}, subRoot = {subroot_list}")
print("Output:", Solution().isSubtree(root, subRoot))