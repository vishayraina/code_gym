# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, d):
            if node:
                d += 1
                ld = dfs(node.left, d)
                rd = dfs(node.right, d)
                d = max(ld, rd)
            return d
        return dfs(root, 0)
