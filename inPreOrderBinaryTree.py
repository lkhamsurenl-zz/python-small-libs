class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def pr(self):
        if self.left is None and self.right is None:
            return str(self.val)
        elif self.left is None:
            return ("({}. NULL {})".format(self.val, self.right.pr()))
        elif self.right is None:
            return  ("({}. {} NULL)".format(self.val, self.left.pr()))
        else:
            return ("({}. {} {})".format(self.val, self.left.pr(), self.right.pr()))

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        return self.recBuild(preorder, 0 , len(preorder) - 1, inorder, 0, len(inorder) - 1)
    def recBuild(self, preorder, preLow, preHigh, inorder, inLow, inHigh):
        if inLow > inHigh:
            return None
        elif inLow == inHigh:
            return TreeNode(inorder[inLow])
        # Find the location of first elt of pre in inorder
        rootIndex = inLow
        while preorder[preLow] is not inorder[rootIndex]:
            rootIndex = rootIndex + 1
        root = TreeNode(preorder[preLow]) # root node
        root.right = self.recBuild(preorder, preLow + (rootIndex - inLow) + 1, preHigh, inorder, rootIndex +1 , inHigh)
        root.left = self.recBuild(preorder, preLow + 1, preLow + (rootIndex - inLow),  inorder, inLow, rootIndex  -1 )
        return root


sol = Solution()
root = sol.buildTree([7,-10,-4,3,-1,2,-8,11], [-4,-10,3,-1,7,11,-8,2])

print root.pr()
