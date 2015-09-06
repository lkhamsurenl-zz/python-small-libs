# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        # do a encoding based on the 0 (left), 1 (right) for each node
        p_enc = self.findEncoding(root, p, 0)
        q_enc = self.findEncoding(root, q, 0)
        # for encodings of the p, q find common binary prefix.
        enc = self.commonPrefix(p_enc, q_enc)
        # return the node with value
        return self.findNode(root, enc)
    def findEncoding(self, root, p, enc):
        if root is None:
            return -1
        if root.val == p.val:
            return enc
        l = self.findEncoding(self, root.left, p, enc << 1)
        r = self.findEncoding(self, root.right, p, (enc << 1) | 1)
        if l >= 0:
            return l
        if r >=0:
            return r
        return -1
    # p, q are encodings of 1 and 0
    def commonPrefix(self, p, q):
        # get the lengths
        p_len = 0
        while p != 0:
            p = p >> 1
            p_len = p_len + 1
        q_len = 0
        while q != 0:
            q = q >> 1
            q_len = q_len + 1
        p_add = p_len - q_len
        q_add = q_len - p_len
        if q_add > 0:
            new_q = q << q_add
            add = q_add
        if p_add > 0:
            new_p = p << p_add
            add = p_add
        return new_p & new_q >> add
    def findNode(self, root, enc):
        if enc == -1:
            return root
        (enc, length) = self.reverse(enc)
        while length != 0:
            dig = enc % 2
            if dig == 1:
                root = root.right
            else:
                root = root.left
            enc = enc >> 1
            length = length - 1
        return root
    def reverse(self, enc):
        curr= enc
        length = 0
        while curr != 0:
            curr = curr
