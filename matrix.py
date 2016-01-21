import copy
class Matrix(object):
	"""
	This file includes a matrix related problems.
	"""

	def spiralMatrix(self, matrix):
		"""
		Given a matrix, return a list in spiral order.
		"""
		output = [] # output list
		row_bottom = len(matrix) - 1
		if row_bottom < 0:
			return output
		col_right = len(matrix[0]) - 1
		row_top = 0
		col_left = 0
		while col_left <= col_right and row_top <= row_bottom:
			for col in range(col_left, col_right + 1):
				if row_top <= row_bottom:
					output.append(matrix[row_top][col])
			# Finished with the row_top
			row_top += 1

			for row in range(row_top, row_bottom + 1):
				if col_left <= col_right:
					output.append(matrix[row][col_right])
			# Finished with the col_right
			col_right -= 1

			for col in range(col_right, col_left - 1, -1):
				if row_top <= row_bottom:
					output.append(matrix[row_bottom][col])
			# Finised with the row_bottom
			row_bottom -= 1

			for row in range(row_bottom, row_top - 1, -1):
				if col_left <= col_right:
					output.append(matrix[row][col_left])
			# Finished with the col_left
			col_left += 1

		return output

	def numOfIslands(self, grid):
		"""
		Given a grid representing land(1) and water(0), find number of Islands.
		"""
		assert len(grid) != 0 and len(grid[0]) != 0,\
			"numOfIslands(grid); grid should be non empty."
		numIslands = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				numIslands += self.__DFS__(grid, i, j)
		return numIslands

	def __DFS__(self, grid, i, j):
		"""
		Traverse the current island for all possible directions.
		"""
		if 0 > i or i >= len(grid) or 0 > j or j >= len(grid[0]) or grid[i][j] == 0:
			return 0 
		grid[i][j] = 0 # mark as visited
		self.__DFS__(grid, i + 1, j)
		self.__DFS__(grid, i - 1, j)
		self.__DFS__(grid, i, j + 1)
		self.__DFS__(grid, i, j - 1)
		return 1

	def rotateClockwise(self, matrix):
		"""
		Rotate given matrix clockwise in place.
		"""
		length = len(matrix)
		if length == 0:
			return matrix
		assert len(matrix) == len(matrix[0]), \
			"Matrix must be square: got ({}, {})".format(len(matrix), len(matrix[0]))
		upper = length / 2 if length % 2 == 0 else length / 2 + 1
		for i in range(upper):
			for j in range(length / 2):
				temp = matrix[i][j]
				matrix[i][j] = matrix[length - j - 1][i]
				matrix[length - j - 1][i] = matrix[length - i - 1][length - j - 1]
				matrix[length - i - 1][length - j - 1] = matrix[j][length - i - 1]
				matrix[j][length - i - 1] = temp

	def longestIncreasingPath(self, matrix):
		"""
		Find longest increasing path length in a given matrix.
		Adding edge for small to big number, we can form DAG, therefore doing
		simple BFS will result in logest path.
		"""
		active = [] # all the active vertices
		level = 0  # current level
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				active.append((i, j))
		while len(active) != 0:
			next_active = [] # next active level
			for (i, j) in active:
				if 0 <= i - 1 < len(matrix) and matrix[i-1][j] > matrix[i][j]:
					next_active.append((i-1, j))
				if 0 <= j - 1 < len(matrix[0]) and matrix[i][j-1] > matrix[i][j]:
					next_active.append((i, j-1))
				if 0 <= i + 1 < len(matrix) and matrix[i+1][j] > matrix[i][j]:
					next_active.append((i+1, j))
				if 0 <= j + 1 < len(matrix[0]) and matrix[i][j+1] > matrix[i][j]:
					next_active.append((i, j+1))
			active = next_active
			level += 1
		return level

#############						TEST						##############
matrix = Matrix()

###################					spiralMatrix				################
for (m, want) in [ ([[1]], [1]), \
					([[1,2,3], [4,5,6], [7,8,9]], [1,2,3,6,9,8,7,4,5]),\
					([[1,2,3,4], [5,6,7,8], [9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7])]:
	got = matrix.spiralMatrix(m)
	assert got == want, \
		"spiralMatrix({}) = {}; want: {}".format(m, got, want)

##############						numOfIslands					##########
for (grid, want) in [ ([[1,0],[0,1]], 2), ([[1,1], [1,0]], 1), ([[1]], 1),\
					([[1,1,0], [1,0,1], [0,1,0]], 3) ]:
	got = matrix.numOfIslands(grid)
	assert got == want, \
		"numOfIslands({}) = {}; want: {}".format(grid, got, want)

for (got, want) in [ ([[1,2], [3,4]], [[3,1],[4,2]]), \
				([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]) ]:
	m = copy.deepcopy(got)
	matrix.rotateClockwise(got)
	assert got == want, \
		"rotateClockwise({}) = {}; want: {}".format(m, got, want)

###################		 longestIncreasingPath  				################
for (m, want) in [ ([[1]], 1), ([[9,9,6], [6,6,8], [2,1,1]], 4),\
					([[3,4,5], [3,2,6], [2,2,1]], 4) ]:
	got = matrix.longestIncreasingPath(m)
	assert got == want, \
		"longestIncreasingPath({}) = {}; want: {}".format(m, got, want)