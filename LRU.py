from heapq import heappush, heappop
from doubleLinkedList import DoubleList, Node
class LRUCache(object):
	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.mapping = {} # key: (value, key_node)
		# Double Linked list of key_nodes. Leftmost element is most recent
		self.doubleList = DoubleList() 
		self.capacity = capacity

	def get(self, key):
		if key not in self.mapping:
			return None
		(value, key_node) = self.mapping[key]
		# Remove from LL
		self.doubleList.remove(key_node)
		# Make it the most recent element
		self.doubleList.appendleft(key_node)
		return value

	def set(self, key, value):
		if key in self.mapping:
			# already exist, just update it in the dict and LL
			(val, key_node) = self.mapping[key]
			# Remove from LL
			self.doubleList.remove(key_node)
			# Make it most recent.
			self.doubleList.appendleft(key_node)
			# Remove the element from the dict
			self.mapping[key] = value
			return 
		if len(self.mapping) == self.capacity:
			# Remove element from the LL and dict
			node_lru = self.doubleList.pop()
			self.mapping.pop(node_lru.val)
		# Add key, value
		key_node = Node(key)
		self.doubleList.appendleft(key_node)
		self.mapping[key] = (value, key_node)

################				TEST 			###################
print("Testing LRU cache")
lru = LRUCache(2)
lru.set(1, 2)
lru.set(2, 3)
assert lru.get(1) == 2
lru.set(3, 4)
print(lru.mapping)






