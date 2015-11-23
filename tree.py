from collections import deque
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

class Tree(object):
	def treeEqual(self, root1, root2):
		if root1 == None and root2 == None:
			return True
		if not (root1 != None and root2 != None):
			return False
		return root1.val == root2.val and self.treeEqual(root1.left, root2.left) and self.treeEqual(root1.right, root2.right) 
	
	def height(self, root):
		if root == None:
			return -1
		return 1 + max(self.height(root.right), self.height(root.left))

	def maxPathSum(self, root):
		"""
		Max path sum in a given tree
		"""
		return self.__recPathSum(root)[1]

	def __recPathSum(self, root):
		"""
		return (maxPathSum in one side with root included, maxPathSum)
		"""
		if root.left == None and root.right == None:
			return (root.val, root.val)
		(l, lm) = self.__recPathSum(root.left) if root.left != None else (0, -float('inf'))
		l = max(0, l) 
		(r, rm) = self.__recPathSum(root.right) if root.right != None else (0, -float('inf'))
		r = max(0, r)
		return (root.val + max(l, r), max(root.val + l + r, lm, rm))

class Codec:
	def ser(self, root):
		"""
		Serializes a given tree in following way: [1,2,null, 3,4, null, null]
		"""
		t = Tree()
		h = t.height(root) # find the height of the tree
		s = ["null"] * (2**(h + 1) - 1)
		self.__recSer(root, s, 0)
		return s
	def __recSer(self, root, s, i):
		if root == None:
			return 
		s[i] = root.val
		self.__recSer(root.left, s, 2 * i + 1)
		self.__recSer(root.right, s, 2 * i + 2)

	def deser(self, s):
		"""
		constructs a tree from a serialized list: [1, 2, null] 
		"""
		# length should be exactly 2^(h + 1) - 1 = len(s)
		return self.__recDeser(s,0)
	def __recDeser(self, s, i):
		if i >= len(s) or s[i] == 'null':
			return None
		root = TreeNode(s[i])
		root.left = self.__recDeser(s, 2 * i + 1)
		root.right = self.__recDeser(s, 2 * i + 2)
		return root

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

class Traversal(object):
	"""
	Pre, In, Level and Post order traversals in tree without using any recursion
	"""
	def levelOrder(self, root):
		if root == None:
			return []
		ordering = []
		q = deque()
		q.appendleft(root)
		q.appendleft('#') # special symbol representing the current level
		while len(q) != 0:
			curr = q.pop()
			if curr == '#' and len(q) == 0:
				break
			elif curr == '#':
				q.appendleft('#') # put it back at the end representing level
			else:
				ordering.append(curr.val)
				if curr.left != None:
					q.appendleft(curr.left)
				if curr.right != None:
					q.appendleft(curr.right)
		return ordering

	def preOrder(self, root):
		ordering = []
		if root == None:
			return ordering
		s = [root]
		while len(s) != 0:
			top = s.pop()
			ordering.append(top.val)
			if top.right != None:
				s.append(top.right)
			if top.left != None:
				s.append(top.left)
		return ordering

	def inOrder(self, root):
		if root == None:
			return []
		s = [(root, 'NEW')] # each element has state associated with it
		ordering = []
		while len(s) != 0:
			(top, state) = s.pop()
			if top.left != None and state == 'NEW':
				s.append((top, 'VISITED')) # add the element back with new state
				s.append((top.left, 'NEW'))
			else: # done with the current element's left side
				ordering.append(top.val)
				if top.right != None:
					s.append((top.right, 'NEW'))
		return ordering

	def postOrder(self, root):
		ordering = []
		if root == None:
			return ordering
		s = [(root, 'NEW')]
		while len(s) != 0:
			(top, state) = s.pop()
			if state == 'NEW':
				# Add the node back with changed state.
				s.append((top, 'DONE'))
				# Then add the right and left nodes, if possible.
				if top.right != None:
					s.append((top.right, 'NEW'))
				if top.left != None:
					s.append((top.left, 'NEW'))
			else:
				ordering.append(top.val)
		return ordering

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


#########					TEST				#################
tree = Tree()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

#############				Serialize 				###################
codec = Codec()
ser = codec.serialize(root)
assert(ser == [1, [2, [], []], [3, [], []]])
deser = codec.deserialize(ser)
assert(tree.treeEqual(deser, root))
ser = codec.ser(root)
assert(ser == [1,2,3])
deser = codec.deser([1,2,3])
assert(tree.treeEqual(deser, root))
print("Serialize test pass!")

#############				BST Kth smallest 				###################
bst = BST()
root = codec.deserialize([7, [3, [1, [], []], [5, [], []]], [25, [10, [], []], []]])
for (target, want) in [(1,1), (2,3), (3,5), (4,7), (5, 10), (6, 25), (7, -1)]:
	got = bst.kthSmallest(root, target)
	assert got == want, \
		"kthSmallest(root, {}) = {}; want {}".format(target, got, want)
print("BST test pass!")

#############				Level Order				###################
traversal = Traversal()
root = codec.deser([1,2,3,"null", 4, 5, "null"])
assert(traversal.levelOrder(root) == [1,2,3, 4, 5])
assert(traversal.inOrder(root) == [2, 4, 1, 5, 3])
assert(traversal.preOrder(root) == [1, 2, 4, 3, 5])
assert(traversal.postOrder(root) == [4,2, 5, 3,1])
print("Traversal test pass!")



