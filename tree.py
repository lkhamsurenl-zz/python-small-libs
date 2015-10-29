class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

def TreeEqual(root1, root2):
	if root1 == None and root2 == None:
		return True
	if not (root1 != None and root2 != None):
		return False
	return root1.val == root2.val and TreeEqual(root1.left, root2.left) and TreeEqual(root1.right, root2.right) 

class Codec:
	def serialize(self, root):
		"""
		Serializes the given TreeNode to [1, [2, [], []], [3, [], []]]
		"""
		if root == None:
			return []
		return [root.val, self.serialize(root.left), self.serialize(root.right)]

	def deserialize(self, data):
		"""
		deserializes the given data, which has the form:
		[1, [2, [], []], [3, [], []]]
		"""
		if len(data) == 0:
			return None
		[ro, l, r] = data
		root = TreeNode(ro)
		root.left = self.deserialize(l)
		root.right = self.deserialize(r)
		return root

#########					TEST				#################
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

#############				Serialize 				###################
codec = Codec()
ser = codec.serialize(root)
assert(ser == [1, [2, [], []], [3, [], []]])
deser = codec.deserialize(ser)
assert(TreeEqual(deser, root))

