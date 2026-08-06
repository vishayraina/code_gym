# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.preorder = []
        def dfs(node):
            if not node:
                self.preorder.append("N")
                return
            self.preorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return ",".join(self.preorder)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        data = data.split(",")
        def dfs():
            if data[self.i] == "N":
                return None
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = dfs()
            self.i += 1
            root.right = dfs()
            return root
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))