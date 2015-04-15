# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        lst = [] # curr flatened lsit
        stack.append([root, 0]) # 0 means pushing first time
        while len(stack) !=0 :
            top = stack[-1] # top element
            if top[1] == 0:
                stack[-1][1] = 1 # change it to visited
                # check elft side
                if top[0].left is not None:
                    stack.append([top[0].left, 0]) # with no visited
            else:
                stack.pop() # remove element
                lst.append(top[0].val)
                if top[0].right is not None:
                    stack.append([top[0].right, 0])
        return lst

sol = Solution()
root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('E')
root.left.left = TreeNode('D')
root.left.right = TreeNode('C')
root.right.left = TreeNode('F')
root.right.right = TreeNode('G')
root.right.right.left = TreeNode('H')
print sol.inorderTraversal(root)
