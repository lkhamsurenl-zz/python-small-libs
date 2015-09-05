class Solution: 
	def spiral(self, arr):
		rowStart = 0 # start row scanning
		colStart = 0 # start col scanning 
		m = len(arr)
		if m == 0:
			return 
		n = len(arr[0])
		rowEnd = m - 1 # end Wall 
		colEnd = n - 1
		# current direction
		isHorizontal = True  # start in the horizontal direction
		isForward = True 
		i = 0 # current row position
		j = 0 # current col position
		while rowStart <= i <= rowEnd and colStart <= j <= colEnd:
			# print current value
			print(arr[i][j])
			# check if hit the wall, if so then update the direction and update wall values
			if isHorizontal and isForward and j == colEnd:
				isHorizontal = False
				rowStart += 1
			elif isHorizontal and not isForward and  j == colStart:
				isHorizontal = False # check in horizontal
				isForward = False
				rowEnd -= 1
			elif not isHorizontal and isForward and i == rowEnd:
				isHorizontal = True
				isForward = False
				colEnd -= 1
			elif not isHorizontal and not isForward and i == rowStart:
				isHorizontal = True
				isForward = True
				colStart += 1
			# increment the values depending on the current direction
			if isHorizontal and isForward:
				j = j + 1
			elif isHorizontal and not isForward:
				j = j - 1
			elif not isHorizontal and isForward:
				i = i + 1
			elif not isHorizontal and not isForward:
				i = i - 1

sol = Solution()
sol.spiral([[1,2,3,4,5], [6,7,8,9,10], [11, 12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]])