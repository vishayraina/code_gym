# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recursion(preorder, inorder):
            if not preorder:
                return None
            root = preorder[0]
            tree = TreeNode(root)
            idx = inorder.index(root)
            tree.left = recursion(preorder[1:idx+1], inorder[:idx])
            tree.right = recursion(preorder[idx+1:], inorder[idx+1:])
            return tree
        return recursion(preorder, inorder)
