# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mps = float("-inf")
        def dfs(node):
            if not node:
                return 0
            lmps = dfs(node.left)
            rmps = dfs(node.right)
            self.mps = max(self.mps, node.val + max(lmps, 0) + max(rmps, 0))
            return max(lmps+node.val, rmps+node.val, node.val)
        dfs(root)
        return self.mps