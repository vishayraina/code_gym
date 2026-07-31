# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                lsame = dfs(node1.left, node2.left)
                rsame = dfs(node1.right, node2.right)
                return (lsame and rsame)
            elif node1 or node2:
                return False
            return True
        return dfs(p,q) 