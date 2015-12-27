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




#############					TEST				##########################


####################			minimumCoins			#######################
for (coins, amount, want) in [ ([2], 1, -1), ([2], 0, 0), ([1,2,5], 11, 3),\
	([3,7,405,436], 8839, 25) ]:
	got = minimumCoins(coins, amount)
	assert got == want, \
		"minimumCoins({}, {}) = {}; want: {}".format(coins, amount, got, want)