# Definition for a  binary tree node
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
    def buildTree(self, inorder, postorder):
        if len(postorder) == 0:
            return None
        return self.recBuild(inorder, 0 , len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def recBuild(self, inorder, inLow, inHigh, postorder, postLow, postHigh):
        if inLow > inHigh:
            return None
        elif inLow == inHigh:
            return TreeNode(inorder[inLow])
        # Find the location of first elt of pre in inorder
        rootIndex = inLow
        while postorder[postHigh] != inorder[rootIndex]:
            rootIndex = rootIndex + 1
        root = TreeNode(postorder[postHigh]) # root node
        root.right = self.recBuild(inorder, rootIndex + 1, inHigh,  postorder, postLow + (rootIndex - inLow), postHigh - 1)
        root.left = self.recBuild(inorder, inLow, rootIndex - 1, postorder, postLow, postLow + (rootIndex - inLow) -1 )
        return root


sol = Solution()
root = sol.buildTree([-4,-10,3,-1,7,11,-8,2], [-4,-1,3,-10,11,-8,2,7])

print root.pr()
