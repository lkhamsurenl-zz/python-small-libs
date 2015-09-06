class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    paths = []
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # clean up the paths
        self.paths = []
        if root != None:
            self.recPath(root, "")
        return self.paths

    def recPath(self, root, curr):
        if root.left is None and root.right is None:
            self.paths.append(curr + str(root.val))
            return
        if root.left != None:
            self.recPath(root.left, curr + str(root.val) + "->")
        if root.right != None:
            self.recPath(root.right, curr + str(root.val) + "->")

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

paths = sol.binaryTreePaths(root)
for path in paths:
    print(path)

root = TreeNode(1)
paths = sol.binaryTreePaths(root)
for path in paths:
    print(path)
