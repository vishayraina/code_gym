# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# diameter is a global variable keeping max
# Recursive call: diameter of the subtree
# Returns: max depth of subtree
# Base case: None = 0
# Parent uses: max(diameter, left_depth + right depth)
# Key insight: each call computs depth and diameter, diameter is updated to global var andmax depth is returned to parent. parent consumes depth and diameter

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0
        def dfs(node):
            nonlocal dia
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            dia = max(dia, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        dfs(root)
        return dia
