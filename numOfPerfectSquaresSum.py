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
			if i not in squares:
				minimal_sq = float('inf')
				# find the index of the number closest but less than i
				max_index = self.binarySearch(i, squares, 0, len(squares) - 1)
				for num_sq in squares[:max_index+1]:
					# num_sq can be repeated in the list
					times = 1
					while times * num_sq <= i:
						minimal_sq = min(minimal_sq, 1 + ls[i - num_sq])
						times += 1
				ls[i] = minimal_sq
		return ls[num]

	def binarySearch(self, num, arr, low, high):
		"""
		Binary binarySearch in arr to find index closest but greater than num
		"""
		if low >= high:
			return low
		mid = low + (high - low) / 2
		# middle is the correct answer
		if arr[mid] > num and arr[mid - 1] <= num:
			return mid
		if arr[mid] < num:
			return self.binarySearch(num, arr, mid + 1, high)
		else:
			return self.binarySearch(num, arr, low, mid - 1)

sol = Solution()
assert(1 == sol.numSquares(1))
assert(1 == sol.numSquares(4))
# 2 = 1 + 1
assert(2 == sol.numSquares(2))
# 9 = 9
assert(1 == sol.numSquares(9))
# 12 = 4 + 4 = 4
assert(3 == sol.numSquares(12))
# 13 = 9 + 4
assert(2 == sol.numSquares(13))
print(sol.numSquares(296))
assert(2 == sol.numSquares(17))
########## Testing binarySearch
sq = [1, 4, 9,16,25,36,49,64,81,100]
assert(1 == sol.binarySearch(3, sq, 0, 9))
assert(2 == sol.binarySearch(5, sq, 0, 9))
assert(1 == sol.binarySearch(5, sq, 0, 1))