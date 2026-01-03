class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right


def buildTree(arr):
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(x) for x in arr]
    for i in range(len(arr)):
        if nodes[i]:
            if 2*i+1 < len(arr): nodes[i].left = nodes[2*i+1]
            if 2*i+2 < len(arr): nodes[i].right = nodes[2*i+2]
    return nodes
tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p_val, q_val = 5, 1

nodes = buildTree(tree)
root = nodes[0]

# find nodes p and q
p = next(n for n in nodes if n and n.val == p_val)
q = next(n for n in nodes if n and n.val == q_val)

lca = Solution().lowestCommonAncestor(root, p, q)

print(f"Input: root = {tree}, p = {p_val}, q = {q_val}")
print("Output:", lca.val)
