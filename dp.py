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

