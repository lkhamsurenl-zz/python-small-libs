# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    sum = 0
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        self.recSum(root, 0) # this should be called first
        return self.sum
    def recSum(self, root, acc):
        if root is None:
            self.sum = self.sum + acc
        if root.left is None and root.right is None: # leaf
            self.sum = self.sum + acc * 10 + root.val
        if root.left is not None:
            self.recSum(root.left, acc * 10 + root.val)
        if root.right is not None:
            self.recSum(root.right, acc * 10 + root.val)

sol = Solution()
node = TreeNode(1)
#node.right = TreeNode(2)
#node.left = TreeNode(3)
#node.left.left = TreeNode(4)
print sol.sumNumbers(node)
