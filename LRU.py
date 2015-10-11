from heapq import heappush, heappop

class LRUCache(object):
	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		# if reached capacity, then invalidate the LRU element
		self.h = [] # (count, key, value)
		self.d = {} # (key, (value, count))
		self.size = 0
		self.cap = capacity
		self.count = 0

	def get(self, key):
		# lookup the d 
		if key in self.d:
			self.count += 1
			# exist, then update count in d by incrementing count
			(v, c) = self.d[key]
			self.d[key] = (v, self.count)
			# also update h by removing first, then push again
			self.h.remove((c, key, v))
			heappush(self.h, (self.count, key, v))
			return v
		else:
			return -1

	def set(self, key, value):
		if key in self.d:
			(v, c) = self.d[key]
			# also update h by removing first, then push again
			self.h.remove((c, key, v))
			return v
		else:
			if self.size == self.cap:
				# remove the element
				(c, k, v) = heappop(self.h)
				# remove from d
				self.d.pop(k, None)
			else:
				self.size += 1
		self.count += 1
		self.d[key] = (value, self.count)
		heappush(self.h, (self.count, key, v))

################				TEST 			###################
print("Testing LRU cache")
lru = LRUCache(10)





