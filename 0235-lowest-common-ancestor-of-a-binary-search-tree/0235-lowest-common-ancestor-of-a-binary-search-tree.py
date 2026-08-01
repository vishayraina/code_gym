# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node, p, q):
            if node:
                if node.val > p.val and node.val > q.val:
                    return dfs(node.left, p, q)
                elif node.val < p.val and node.val < q.val:
                    return dfs(node.right, p, q)
                elif node.val == p.val or node.val == q.val or (node.val > p.val and node.val < q.val) or (node.val < p.val and node.val > q.val):
                    return node
        return dfs(root, p, q)