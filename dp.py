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

def minPathSum(grid):
	"""
	Find minimum path sum on grid, starting @ top left to bottom right.
	"""
	MPS = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
	# Base:
	for i in range(1, len(grid)):
		MPS[i][0] += MPS[i-1][0]
	for j in range(1, len(grid[0])):
		MPS[0][j] += MPS[0][j - 1]
	# Recursive case:
	for i in range(1, len(grid)):
		for j in range(1, len(grid[0])):
			MPS[i][j] = grid[i][j] + min(MPS[i-1][j], MPS[i][j-1])
	return MPS[len(grid) - 1][len(grid[0]) - 1]

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

def longestIncreasingSubsequence(lst):
	"""
	Find length of the longestIncreasingSubsequence in a list.
	"""
	# LIS[i][j] = length of longestIncreasingSubsequence in 0..i s.t smaller
	# than lst[j]
	l = len(lst)
	lst.append(float('inf'))
	LIS = [[0 for j in range(l + 1)] for i in range(l)]
	# Base case:
	for i in range(l + 1):
		LIS[0][i] = 1 if lst[i] > lst[0] else 0
	# Recursive case:
	for i in range(1, l):
		for j in range(0, l + 1):
			LIS[i][j] = LIS[i - 1][j]
			if lst[i] < lst[j]:
				LIS[i][j] = max(LIS[i][j], 1 + LIS[i-1][i])
	return LIS[l-1][l]

def houseRob(lst):
	"""
	Given lst of houses with money on each, find maximal money one can rob.
	adjacent houses have security system connected and it will automatically
	contact the police if two adjacent houses were broken into on the same night.
	"""
	# HR[i + 1] maximum money possible to rob btw houses 0 to i
	HR = [0 for i in range(len(lst) + 1)]
	# Base case:
	HR[0] = 0
	HR[1] = lst[0]
	# Recursive case:
	for i in range(2, len(lst) + 1):
		HR[i] = max(lst[i-1] + HR[i - 2], HR[i-1])
	return HR[len(lst)]

def interleavingStrings(s1, s2, s3):
	"""
	Check if interleaving s1 and s2 can form s3.
	"""
	if (len(s1) + len(s2)) != len(s3):
		return False # lengths do not add up.
	# IS[i][j] = True <=> interleaving s1[:i] and s2[:j] can form s3[:i + j]
	IS = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
	# Base case:
	for i in range(len(s1) + 1):
		IS[i][0] = s1[:i] == s3[:i]
	for j in range(len(s2) + 1):
		IS[0][j] = s2[:j] == s3[:j]
	# Recursive case:
	for i in range(1, len(s1) + 1):
		for j in range(1, len(s2) + 1):
			if s1[i - 1] == s3[i + j - 1]:
				IS[i][j] = IS[i][j] or IS[i - 1][j]
			if s2[j - 1] == s3[i + j - 1]:
				IS[i][j] = IS[i][j] or IS[i][j - 1]
	return IS[len(s1)][len(s2)]

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

####################			MinPathSum			###########
for (grid, want) in [ ([[1]], 1), ([[0,0,0],[10,1,0],[0,0,0]], 0) ]:
	got = minPathSum(grid)
	assert got == want, \
		"minPathSum({}) = {}; want: {}".format(grid, got, want)

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

####################			longestIncreasingSubseq		       ###########
for (lst, want) in [ ([1], 1), ([1,-1,2], 2), ([1,-1,3,20], 3),\
	([10, 9, 2, 5, 3, 7, 101, 18], 4) ]:
	got = longestIncreasingSubsequence(lst)
	assert got == want, \
		"longestIncreasingSubsequence({}) = {}; want: {}".format(lst, got, want)

####################			houseRobb					       ###########
for (lst, want) in [ ([1], 1), ([4,3,1], 5), ([1,1,3,20], 21),\
	([10, 9, 2, 5, 3, 7, 101, 18], 116) ]:
	got = houseRob(lst)
	assert got == want, \
		"houseRob({}) = {}; want: {}".format(lst, got, want)

####################			Interleaving Strings  	     		###########
for (s1, s2, s3, want) in [ ("","", "", True), ("","xyz","xyz", True), \
	("abc", "", "abc", True), ("a", "b", "c", False), ("a", "b", "ba", True), \
	("a", "b", "ab", True), ("axz", "byd", "dybaxz", False) ]:
	got = interleavingStrings(s1, s2, s3)
	assert got == want, \
		"interleavingStrings({},{},{})= {}; want: {}".format(s1,s2,s3,got,want)
