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

	def flatten(self, root):
		"""
		Flatten the given tree to all the right pointers
		"""
		if root == None or (root.left == None and root.right == None):
			return [root, root]
		[left_start, left_end] = self.flatten(root.left)
		[right_start, right_end] = self.flatten(root.right)
		# Connect the pointers
		root.left = None
		if left_start != None:
			root.right = left_start
			left_end.right = right_start
		# Find the end
		if right_end != None:
			end = right_end
		elif left_end != None:
			end = left_end
		else:
			end = root
		return [root, end]

class BST(object):
	def kthSmallest(self, root, k):
		"""
		Find the kthSmallest element in the BST, using in-order traversal
		in-order traversal visit elements in BST smallest to largest order
		"""
		if root == None:
			return -1 # no matching
		m = {} # node to index mapping, also indicate which elements has been visited
		index = 0 # current available index 
		stack = [root] # in-order traversal stack
		while len(stack) != 0:
			top = stack[-1] # top element
			if top.left != None and top.left not in m:
				stack.append(top.left)
			else:
				stack.pop() # remove the top element
				index += 1
				if index == k:
					# we found the kth smallest element
					return top.val
				m[top] = index
				if top.right != None:
					stack.append(top.right)
		return -1 # k is out of bound

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
print("Serialize test pass!")

#############				BST Kth smallest 				###################
bst = BST()
root = codec.deserialize([7, [3, [1, [], []], [5, [], []]], [25, [10, [], []], []]])
assert(bst.kthSmallest(root, 1) == 1)
assert(bst.kthSmallest(root, 2) == 3)
assert(bst.kthSmallest(root, 3) == 5)
assert(bst.kthSmallest(root, 4) == 7)
assert(bst.kthSmallest(root, 5) == 10)
assert(bst.kthSmallest(root, 6) == 25)
assert(bst.kthSmallest(root, 7) == -1)

print("BST tests pass!")