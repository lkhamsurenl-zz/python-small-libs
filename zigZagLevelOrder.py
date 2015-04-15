# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        queue = deque()
        queue.appendleft(root)
        queue.appendleft('#')
        lst = [[]]
        shouldBeReversed = False
        while len(queue) != 0:
            top = queue.pop() # right end element
            if top == '#' and len(queue) != 0:
                queue.appendleft(top)
                if shouldBeReversed:
                    print "shoudl be reve"
                    lst[-1].reverse() # curr level si done, reverse it
                lst.append([]) # there is a new level starting
                shouldBeReversed = not shouldBeReversed
            elif top  != '#':
                lst[-1].append(top.val) # add to the last list
                if top.left is not None:
                    queue.appendleft(top.left) # add left side
                if top.right is not None:
                    queue.appendleft(top.right) # add right side
        # check for the last level, if it should be reversed
        if shouldBeReversed:
            lst[-1].reverse()
        return lst

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print sol.zigzagLevelOrder(root)
