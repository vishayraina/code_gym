# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float("-inf")
        def dfs(node):
            nonlocal maxsum
            if node:
                leftsum = dfs(node.left)
                rightsum = dfs(node.right)
                maxsum = max(max(leftsum, 0) + max(rightsum, 0) + node.val, maxsum)
                return max(node.val, node.val+leftsum, node.val+rightsum)
            return 0
        dfs(root)
        return maxsum