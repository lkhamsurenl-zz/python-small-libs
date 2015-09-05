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

################################ TEST  ###############################################
sol = Solution()
################################ TEST  ###############################################
print("Testing singleNumber")
assert(2 == sol.singleNumber([1,2,3,1,3]))
assert(1 == sol.singleNumber([1,-2,-2,3,3]))
assert(0 == sol.singleNumber([0,1,1]))
################################ TEST  ###############################################
print("Testing singleNumber2")
print(sol.singleNumber2([1,2,3,3]))
assert(set([1,2]) == set(sol.singleNumber2([1,2,3,3,4,4])))

