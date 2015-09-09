# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def toString(self):
		if self == None:
			return ""
		if self.next == None:
			return self.val
		return "{}->{}".format(self.val, self.next.toString())

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	
class Solution(object):
	def sortedListToBST(self, head):
		"""
		Given a sorted list, convert to a BST balanced
		"""
		dummy = ListNode(-1)
		dummy.next = head
		return self.recBST(dummy)

	def recBST(self, head):
		if head == None:
			return None
		if head.next == None:
			return TreeNode(head.val)
		middle = self.findMiddle(head)
		root = middle.next
		middle.next = None
		second = root.next 
		root.next = None
		left = self.recBST(head)
		right = self.recBST(second)
		r = TreeNode(root.val)
		r.left = left
		r.right = right
		# remove the leftmost node from the tree
		return self.removeSmallest(r)


	def findMiddle(self, head):
		slow = head
		fast = head
		while fast.next != None and fast.next.next != None:
			slow = slow.next 
			fast = fast.next.next
		return slow
	
	def bstToString(self, root):
		if root == None:
			return ""
		return "({}. left: {}, right: {})".format(root.val, self.bstToString(root.left), self.bstToString(root.right))

	def removeSmallest(self, root):
		if root == None:
			return None
		if root.left == None:
			return root.right
		parent = root
		child = root.left
		while child.left != None:
			child = child.left
			parent = parent.left
		parent.left = child.right
		return root

################## TEST ###############################

sol = Solution()

################### Print ListNode ###########################

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print(head.toString())

################### Print ListNode ###########################

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print(sol.bstToString(sol.sortedListToBST(head)))


