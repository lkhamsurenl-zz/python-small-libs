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


#############						TEST						##############
matrix = Matrix()

###################					spiralMatrix				################
for (m, want) in [ ([[1]], [1]), \
					([[1,2,3], [4,5,6], [7,8,9]], [1,2,3,6,9,8,7,4,5]),\
					([[1,2,3,4], [5,6,7,8], [9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7])]:
	got = matrix.spiralMatrix(m)
	assert got == want, \
		"spiralMatrix({}) = {}; want: {}".format(m, got, want)