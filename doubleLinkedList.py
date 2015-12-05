class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

class DoubleList:
	def __init__(self):
		self.head = Node(-1)
		self.tail = Node(-1)
		# connect head and tail
		self.head.next = self.tail
		self.tail.prev = self.head

	def __str__(self):
		if self.head == self.tail:
			return ""
		output = ""
		curr = self.head.next
		while curr.next != self.tail:
			output += "{} <-> ".format(curr.val)
			curr = curr.next
		if curr != None:
			output += str(curr.val)
		return output

	def fromList(self, lst):
		if len(lst) == 0:
			return
		curr = self.head
		for l in lst:
			node = Node(l)
			self.__link__(curr, node)
			curr = curr.next

	def __link__(self, l1, l2):
		l1.next = l2
		l2.prev = l1

	def appendleft(self, node):
		# Given a node, append left
		# Hold onto the next of head.
		temp = self.head.next
		# head <-> node
		self.__link__(self.head, node)
		# node <-> temp
		self.__link__(node, temp)

	def appendright(self, node):
		# Append at the end
		temp = self.tail.prev
		# temp <-> node
		self.__link__(temp, node)
		# node <-> self.tail
		self.__link__(node, self.tail)

	def pop(self):
		if self.head == self.tail:
			return None
		node = self.tail.prev
		self.remove(node)
		return node

	def remove(self, node):
		# Given a node, remove from the DoubleList
		prev = node.prev
		next = node.next
		# prev <-> next
		self.__link__(prev, next)

######							TES 							#############
doubleList = DoubleList()
n1 = Node(1)
doubleList.appendleft(n1)
n2 = Node(2)
doubleList.appendleft(n2)
n3 = Node(3)
doubleList.appendright(n3)
print doubleList
doubleList.remove(n1)
print doubleList
doubleList.pop()
print doubleList

