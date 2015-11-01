def rotate(matrix, n):
	if n == 0:
		return # base
	# if n is odd, then just rotating 4 pixels will result in no rotation for
	# last layer
	add = 1 if n % 2 == 1 else 0 
	for i in range(n /2 + add):
		for j in range(n / 2):
			temp = matrix[n - 1- j][i]
			matrix[n -1 -j][i] = matrix[n - 1- i][n - 1 - j]
			matrix[n - 1 - i][n - 1- j] = matrix[j][n - 1 -i]
			matrix[j][n - 1 -i] = matrix[i][j]
			matrix[i][j] = temp


def rotateLayer(matrix, n):
	if n == 0:
		return 
	for i in range(n/2):
		for j in range(n - 2 * i - 1):
			# size of the current layer
			size = n - 2 * i - 1
			# swap the edge values
			temp = matrix[size - j + i][0 + i]
			matrix[size - j + i][0 + i] = matrix[size + i][size - j + i]
			matrix[size + i][size - j + i] = matrix[j + i][size + i]
			matrix[j + i][size + i] = matrix[0 + i][j + i]
			matrix[0 + i][j+i] = temp

for matrix in  [[[1,2,3, 4], [5,6, 7, 8], [9, 10, 11, 12], [13,14,15,16]], [[1,2,3], [4,5,6], [7,8,9]]]:
	rotate(matrix, len(matrix))
	print(matrix)

for matrix in [[[1,2,3, 4], [5,6, 7, 8], [9, 10, 11, 12], [13,14,15,16]], [[1,2,3], [4,5,6], [7,8,9]]]:
	rotate(matrix, len(matrix))
	print(matrix)
