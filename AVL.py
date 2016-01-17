from tree import Codec

class TreeNode(object):
	def __init__(self, value):
		self.val = value
		self.right = None
		self.left = None
		# TODO(lkhamsurenl): Implement a new version w/o using parent.
		self.parent = None

class AVL(object):
	def __init__(self):
		"""
		Initialize an empty tree.
		"""
		self.root = None
		# Codec is used for serializing the given AVL tree.
		self.codec = Codec()

	def serialize(self):
		return self.codec.ser(self.root)

	def get(self, value):
		"""
		Get node with value in the tree, return None if doesn't exist.
		"""
		return self.__getRec__(self.root, value)

	def __getRec__(self, node, value):
		if node == None or node.val == value:
			return node
		if node.val < value:
			return self.__getRec__(node.right, value)
		return self.__getRec__(node.left, value)

	def add(self, value):
		"""
		Add node with value to the tree, return nothing.
		NOTE (lkhamsurenl): Adding node can make the tree unbalanced.
		"""
		new_node = TreeNode(value)
		if self.root == None:
			self.root = new_node
		else:
			self.__addRec__(self.root, new_node)

	def __addRec__(self, node, new_node):
		"""
		Assume node is never None.
		"""
		if node.val < new_node.val and node.right == None:
			node.right = new_node
			new_node.parent = node
		elif node.val > new_node.val and node.left == None:
			node.left = new_node
			new_node.parent = node
		elif node.val < new_node.val:
			self.__addRec__(node.right, new_node)
		else:
			self.__addRec__(node.left, new_node)
		self.__balance__(node)

	def delete(self, value):
		"""
		Remove node with value from the tree, return nothing.
		NOTE (lkhamsurenl): Removing node can make the tree unbalanced.
		"""
		node = self.get(value) # Get the node with value.
		pair = self.__getRightLeftmost__(node)
		# swap the values:
		if pair == None:
			parent_node = self.__ejectRightLeaf__(node)
		else:
			temp = node.val
			node.val = pair.val
			pair.val = temp
			parent_node = self.__ejectRightLeaf__(pair)
		# Move up the ladder and balance if necessary.
		while parent_node != None:
			self.__balance__(parent_node)
			parent_node = parent_node.parent

	def __ejectRightLeaf__(self, leaf):
		# Remove the node:
		parent = leaf.parent
		if parent == None:
			self.root = leaf.left
		elif parent.left == leaf:
			parent.left = leaf.left
		else:
			parent.right = leaf.right
		return parent

	def __getRightLeftmost__(self, node):
		if node.right == None:
			return None
		l = node.right 
		while l.left != None:
			l = l.left 
		return l


	def __balance__(self, node):
		"""
		Balance tree rooted @ node, if not already.
		"""
		heightDiff = self.__getHeight__(node.left) - self.__getHeight__(node.right)
		if abs(heightDiff) <= 1:
			return
		if heightDiff > 1:
			# Left side is taller: 
			self.__rotateRight__(node)
		else:
			# Right side is taller, so rotate left.
			self.__rotateLeft__(node)

	def __rotateRight__(self, node):
		"""
		Rotate the given tree rooted @ node to right.
		"""
		l = node.left

		node.left = l.right
		if l.right != None:
			l.right.parent = node
		
		l.right = node
		# fix the parent pointer
		p = node.parent
		if p == None:
			self.root = l # since node was the root if AVL
		elif p.left == node:
			p.left = l
		else:
			p.right = l
		l.parent = p
		# Node parent should be l.
		node.parent = l

	def __rotateLeft__(self, node):
		"""
		Rotate the given tree rooted @ node to right.
		"""
		r = node.right

		node.right = r.left
		if r.left != None:
			r.left.parent = node

		r.left = node
		# fix the parent pointer.
		p = node.parent
		if p == None: # node is a root of AVL.
			self.root = r
		elif p.left == node:
			p.left = r
		else:
			p.right = r
		r.parent = p
		# Node parent should be r.
		node.parent = r

	def __getHeight__(self, node):
		if node == None:
			return -1
		return 1 + max(self.__getHeight__(node.left), \
			self.__getHeight__(node.right))

#########					TEST				#################
avl = AVL()
avl.add(1)
avl.add(2)
avl.add(3)
# Check it's balanced when added 3 elements.
assert(avl.serialize() == [2,1,3])

# Check get is correct on existing and non-existing values.
assert(avl.get(1).val == 1)
assert(avl.get(3).val == 3)
assert(avl.get(4) == None)
#
avl.add(4)
avl.add(-4)
avl.add(-7)
# Ensure tree is still balanced.
got = avl.serialize()
want = [2,-4,3,-7,1,"null",4]
assert got == want, \
	"{}; want: {}".format(got, want)

# Delete leaf
avl.delete(1)
got = avl.serialize()
want = [2,-4,3,-7,"null","null",4]
assert got == want, \
	"{}; want: {}".format(got, want)

# Delete root
avl.delete(2)
got = avl.serialize()
want = [3,-4,4,-7,"null","null","null"]
assert got == want, \
	"{}; want: {}".format(got, want)
