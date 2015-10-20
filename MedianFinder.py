from heapq import heappush, heappop
class MedianFinder:
	"""
	Finds the median of the streaming numbers
	"""
	def __init__(self):
		# min heap holds elements greater than the median
		self.minheap = []
		self.minsize = 0
		# max heap holds median and smaller elements
		self.maxheap = []
		self.maxsize = 0
	def addNum(self, num):
		# INVARIANT: self.maxsize >= self.minsize
		if self.maxsize == 0 or -self.maxheap[0] >=num:
			heappush(self.maxheap, -num)
			self.maxsize += 1
		else:
			heappush(self.minheap, num)
			self.minsize += 1
		# INVARIANT: maxheap always holds the median
		if self.maxsize - self.minsize > 1:
			heappush(self.minheap, -heappop(self.maxheap))
			self.minsize += 1
			self.maxsize -= 1
		elif self.minsize > self.maxsize:
			heappush(self.maxheap, -heappop(self.minheap))
			self.minsize -= 1
			self.maxsize += 1
	def findMedian(self):
		try: 
			if self.maxsize == self.minsize:
				return float(self.minheap[0] - self.maxheap[0]) / 2
			else:
				return -self.maxheap[0]
		except:
			raise("Illegal operation")


m = MedianFinder()
m.addNum(6)
assert(m.findMedian() == 6)
m.addNum(10)
assert(m.findMedian() == 8)
m.addNum(2)
assert(m.findMedian() == 6)
m.addNum(6)
assert(m.findMedian() == 6)
m.addNum(5)
assert(m.findMedian() == 6)
m.addNum(0)
assert(m.findMedian() == 5.5)

