class Solution(object):
	def numSquares(self, num):
		"""
		Find least numebr of squares add up to the given number

		"""
		squares = []
		i = 1
		while i * i <= num:
			squares.append(i * i)
			i += 1
		ls = [0 for i in range(num + 1)]
		# base
		for i in squares:
			ls[i] = 1
		# recursive 
		for i in range(1, num + 1):
			if i not in ls:
				minimal_sq = float('inf')
				# find the index of the number closest but less than i
				max_index = self.binarySearch(i, squares, 0, len(squares) - 1)
				for num_sq in squares[:max_index]:
					minimal_sq = min(minimal_sq, 1 + ls[i - num_sq])
				ls[i] = minimal_sq
		return ls[num]

	def binarySearch(self, num, arr, low, high):
		"""
		Binary binarySearch in arr to find index closest but greater than num
		"""
		if low >= high:
			return low
		mid = low + (high - low) / 2
		if arr[mid] > num and arr[mid - 1] <= num:
			return mid
		if arr[mid] < num:
			return self.binarySearch(num, arr, mid, high)
		else:
			return self.binarySearch(num, arr, low, mid)

sol = Solution()
assert(1 == sol.numSquares(1))
assert(1 == sol.numSquares(4))
assert(2 == sol.numSquares(2))
