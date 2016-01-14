class Solution:
	def singleNumber(self, nums):
		"""
		Given array of integers, only one of them appears once and all the others appear exactly twice. 
		Find the singleNumber
		"""
		# xor operation will cancel out all the numbers appearing exactly twice
		xor = 0
		for num in nums:
			xor ^= num
		return xor

	def singleNumber2(self, nums):
		"""
		Given an array of integers, exactly two appear once and all others exactly twice. Find numbers
		"""
		# Do xor of all nums to find the last digit differ
		xor = 0
		for num in nums:
			xor ^= num
		# find last portion that differ for two unique numbers (it always exist otherwise numbers would not be same)
		# xor = 101011000
		# xor ^ (xor -1) + 1 === 10000
		diff = ((xor ^ (xor - 1)) + 1)>> 1
		groupA = 0
		groupB = 0
		for num in nums:
			if num & diff:
				groupA ^= num
			else:
				groupB ^= num
		return [groupA, groupB]

################################ TEST  #########################################
sol = Solution()
################################ TEST  #########################################
for (want, lst) in [(2, [1,2,3,1,3]), (1, [1,-2,-2,3,3]), (0, [0,1,1])]:
	got = sol.singleNumber(lst)
	assert got == want, \
		"singleNumber({}) = {}; want: {}".format(lst, got, want)

################################ TEST  #########################################
for (lst, want) in [([1,2,3,3], [1,2])]:
	got = sol.singleNumber2(lst)
	assert set(got) == set(want), \
		"singleNumber2({}) = {}; want: {}".format(lst, got, want)
