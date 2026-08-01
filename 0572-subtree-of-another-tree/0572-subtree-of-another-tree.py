# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(node1, node2):
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                lsame = same_tree(node1.left, node2.left)
                rsame = same_tree(node1.right, node2.right)
                return (lsame and rsame)
            elif node1 or node2:
                return False
            return True
        def dfs(node1, node2):
            if node1 and node2:
                if same_tree(node1, node2):
                    return True
                l = dfs(node1.left, node2)
                r = dfs(node1.right, node2)
                return l or r
            elif node1 or node2:
                return False
        return dfs(root, subRoot)
        