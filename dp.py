def minimumCoins(coins, amount):
	"""
	Find minimum number of coins needed to form amount.
	"""
	MC = [amount + 1] * (amount + 1) # Min coin needed to form amount value.
	# Base case.
	MC[0] = 0 
	# Recursive case.
	for i in range(1, amount + 1):
		for coin in coins:
			if coin <= i:
				MC[i] = min(MC[i], 1 + MC[i - coin])
	return MC[amount] if MC[amount] != amount + 1 else - 1

def uniquePaths(m, n):
	"""
	Robot is starting in top left corner of a grid, figure out how many ways
	can get to the bottom right.
	Robot can only go right or down.
	"""
	UP = [[0 for j in range(n)] for i in range(m)]
	# Base case:
	for i in range(m):
		UP[i][0] = 1
	for j in range(n):
		UP[0][j] = 1
	# Recursive case:
	for i in range(1, m):
		for j in range(1, n):
			UP[i][j] = UP[i - 1][j] + UP[i][j - 1]
	return UP[m - 1][n - 1]

def uniquePathsWithObstacles(obstacleGrid):
	"""
	Robot starts in top left corner of obstacleGrid, figure out # ways to bottom
	right. Robot can go right and down, and obstacleGrid 1 means obstacle.
	"""
	m = len(obstacleGrid)
	if m == 0:
		return 0
	n = len(obstacleGrid[0])
	UPO = [[0 for j in range(n)] for i in range(m)] # # of unique paths with obstacles.
	# Base case:
	UPO[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
	for i in range(1, m):
		if obstacleGrid[i][0] == 0:
			UPO[i][0] = UPO[i - 1][0]
	for j in range(1, n):
		if obstacleGrid[0][j] == 0:
			UPO[0][j] = UPO[0][j - 1]

 	# Recursive case:
 	for i in range(1, m):
 		for j in range(1, n):
 			if obstacleGrid[i][j] == 0:
 				UPO[i][j] = UPO[i][j - 1] + UPO[i - 1][j]

 	return UPO[m - 1][n - 1]

def maxSum(lst):
	"""
	Find a maximal contingent sum.
	"""
	MS = [0 for i in range(len(lst))] # max sum in list[0:i]
	MSI = [0 for i in range(len(lst))] # max sum including s.t next # is inc.
	# Base case:
	MS[0] = lst[0]
	MSI[0] = max(0, lst[0])
	# Recursive case:
	for i in range(1, len(lst)):
		MSI[i] = max(MSI[i-1] + lst[i], 0)
		MS[i] = max(MS[i - 1], lst[i] + MSI[i - 1])
	return MS[len(lst) - 1]

def editDistance(word1, word2):
	"""
	Find a edit distance btw 2 words, given operations: insert, delete, or
	replace a char in a word.
	"""
	# ED[i][j] is a min dist btw word1[0:i] and word2[0:j] not inclusive.
	ED = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
	# Base case:
	for i in range(len(word1) + 1):
		ED[i][0] = i
	for j in range(len(word2) + 1):
		ED[0][j] = j
	# Recursive case:
	for i in range(1, len(word1) + 1):
		for j in range(1, len(word2) + 1):
			if word1[i-1] == word2[j-1]:
				ED[i][j] = min(ED[i-1][j-1], ED[i][j-1] + 1, ED[i-1][j] + 1)
			else:
				ED[i][j] = 1 + min(ED[i-1][j-1], ED[i][j-1], ED[i-1][j])
	return ED[len(word1)][len(word2)]

#############					TEST				##########################


####################			minimumCoins			#######################
for (coins, amount, want) in [ ([2], 1, -1), ([2], 0, 0), ([1,2,5], 11, 3),\
	([3,7,405,436], 8839, 25) ]:
	got = minimumCoins(coins, amount)
	assert got == want, \
		"minimumCoins({}, {}) = {}; want: {}".format(coins, amount, got, want)

####################			uniquePaths			#######################
for (m, n, want) in [ (1, 1, 1), (2, 1, 1), (2, 3, 3),(3,4,10) ]:
	got = uniquePaths(m, n)
	assert got == want, \
		"uniquePaths({}, {}) = {}; want: {}".format(m, n, got, want)

####################			UniquePathsWithObstacles			###########
for (grid, want) in [ ([[1]], 0), ([[0]], 1), ([[0,0,0],[0,1,0],[0,0,0]], 2),\
	([[0,1,0],[0,0,0],[1,0,0]], 2) ]:
	got = uniquePathsWithObstacles(grid)
	assert got == want, \
		"uniquePathsWithObstacles({}) = {}; want: {}".format(grid, got, want)

####################			maxSum				    			###########
for (lst, want) in [ ([1], 1), ([1,-1,2], 2), ([1,-1,3,-20], 3),\
	([-2,1,-3,4,-1,2,1,-5,4], 6) ]:
	got = maxSum(lst)
	assert got == want, \
		"maxSum({}) = {}; want: {}".format(lst, got, want)

####################			editDistance  	    			###########
for (word1, word2, want) in [ ("a","b", 1), ("xy","xyz",1), ("abc","abc",0),\
	("abc", "axc", 1) ]:
	got = editDistance(word1, word2)
	assert got == want, \
		"editDistance({}, {}) = {}; want: {}".format(word1, word2, got, want)
