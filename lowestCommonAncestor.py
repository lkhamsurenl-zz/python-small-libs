class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

class Solution:
	def lowestCommonAncestor(self, root, p, q):
		"""
		Given p, q TreeNodes find their lowestCommonAncestor in tree rooted at root
		"""
		enc_p = self.findEncoding(root, p, "")
		enc_q = self.findEncoding(root, q, "")
		# find leading common encoding 
		common = ""
		for i in range(min(len(enc_p), len(enc_q))):
			if enc_p[i] != enc_q[i]:
				break # no longer match
			else:
				common += enc_p[i] # increment
		return self.findEncodingNode(root, common)

	def findEncoding(self, root, p, enc_curr):
		"""
		Find string encoding of p in tree starting at root ( left  = 0, right = 1)
		"""
		# traverse the tree to find the encoding 
		if root is None:
			return None
		if root == p:
			return enc_curr
		right = self.findEncoding(root.right, p, enc_curr + "1")
		return right if right != None else self.findEncoding(root.left, p, enc_curr + "0")

	def findEncodingNode(self, root, encoding):
		"""
		Given encoding, follow it to find the node (left = 0, right = 1)
		"""
		if root == None or len(encoding) == 0:
			return root
		if encoding[0] == '1':
			return self.findEncodingNode(root.right, encoding[1:])
		else:
			return self.findEncodingNode(root.left, encoding[1:])


###############################     TEST       #####################################
sol = Solution()

###############################  lowest common ancestor   #####################################
print("Testing lowest common ancestor in binary tree")
root = TreeNode(1)
root.right = TreeNode(2)
assert(1 == sol.lowestCommonAncestor(root, root, root.right).val)
root = TreeNode(3)
root.right = TreeNode(8)
root.right.left = TreeNode(11)
root.right.left.right = TreeNode(4)
root.left = TreeNode(7)
root.left.left = TreeNode(9)
root.left.right = TreeNode(5)
assert(3 == sol.lowestCommonAncestor(root, root.right.left.right, root.left.left).val)
