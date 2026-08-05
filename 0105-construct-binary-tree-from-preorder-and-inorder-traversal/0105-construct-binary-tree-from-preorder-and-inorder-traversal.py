# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.imap = {}
        for i in range(len(inorder)):
            self.imap[inorder[i]] = i
        def dfs(pl, pr, il, ir):
            if pl > pr or il > ir:
                return None
            root = TreeNode(preorder[pl])
            idx = self.imap[root.val]
            num_left = idx - il
            root.left = dfs(pl+1, pl+num_left, il, il+num_left-1)
            root.right = dfs(pl+num_left+1, pr, il+num_left+1, ir)
            return root
        return dfs(0, len(preorder)-1, 0, len(inorder)-1)