# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """
        :type root: TreeNode
        :rtype: string
        """
        ser = ""
        def dfs(node):
            nonlocal ser
            if node:
                ser += str(node.val) + ","
                dfs(node.left)
                dfs(node.right)
                return ser
            ser += "N,"
            return ser
        dfs(root)
        return ser
        
        
    def deserialize(self, data):
        """
        :type root: string
        :rtype: TreeNode
        """
        data = data.strip(",").split(",")
        n = len(data)
        self.i = 0
        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))