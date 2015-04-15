from collections import deque
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        dummy = TreeLinkNode(-1) #special symbol
        q = deque()
        q.append(dummy)
        q.append(root)
        while len(q) != 0:
            top = q.popleft()
            if top.val == -1   and len(q) != 0:
                q.append(top)
            elif top.val != -1:
                print q[-1].val
                top.next = q[-1] if len(q) != 0 and q[-1].val != 0 else None
                if top.right is not None:
                    q.append(top.right)
                if top.left is not None:
                    q.append(top.left)

sol = Solution()
head = TreeLinkNode(1)
head.left = TreeLinkNode(2)
head.right = TreeLinkNode(3)
sol.connect(head)
print head.next == None
print head.right.next == 3
print head.left.next == None
