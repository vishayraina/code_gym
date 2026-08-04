# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recursion(pl, pr, il, ir):
            if pl > pr or il > ir:
                return None
            
            parent = preorder[pl]
            root = TreeNode(parent)
            idx = inorder.index(parent)
            numsLeft = idx - il
            root.left = recursion(pl+1, pl+numsLeft, il, il+numsLeft-1)
            root.right = recursion(pl+numsLeft+1, pr, il+numsLeft+1, ir)
            return root
        return recursion(0, len(preorder)-1, 0, len(preorder)-1)
