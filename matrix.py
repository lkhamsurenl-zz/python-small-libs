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