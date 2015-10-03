import copy
import itertools
class Solution(object):
	def combinationSum(self, candidates, target):
		globalList = []
		candidates.sort()
		self.recCom(candidates, 0, target, [], globalList)
		return globalList

	def recCom(self, candidates, index, target, currList, globalList):
		if target < 0 or index == len(candidates):
			return
		if target == 0:
			globalList.append(currList)
			return
		for i in xrange(index, len(candidates)):
			self.recCom(candidates, i, target - candidates[i], currList + [candidates[i]], globalList)

	def combinationSum2(self, candidates, target):
		globalList = []
		candidates.sort()
		self.dfs(candidates, target, [], globalList)
		globalList.sort()
		return list(k for k, _ in itertools.groupby(globalList))

	def dfs(self, nums, target, currList, globalList):
		if target < 0 or len(nums) == 0:
			return 
		if target == 0:
			currList.sort()
			globalList.append(currList)
			return
		for num in nums:
			newNums = copy.deepcopy(nums)
			newNums.remove(num)
			self.dfs(newNums, target - num, currList + [num], globalList)

	def combinationSum3(self, n, k):
		"""
		Given n, find k digits between 1 to 9 add up to n such that no digit is repeated.
		1 <= k <= 9
		1 <= n <= 45
		"""
		result = []
		if not (1 <= k <= 9 and 1<= n <= 45):
			return result
		self.digitSum(n, k, [], 0, result)
		return result

	def digitSum(self, n, k, currList, index, result):
		"""
		recursive function to compute all ways to get the n
		@param n: number to add up to
		@param k: number of digits allowed to use
		@param currList: current list of numbers used
		@param index: can use digits between index < i <= 9
		@param result: overall result of all possible answer
		"""
		if index > 9 or k < 0 or (n != 0 and k == 0) or (n == 0 and k != 0):
			return # backtrack
		if n == 0 and k == 0:
			result.append(currList)
			return
		for i in range(index + 1, 10):
			self.digitSum(n - i, k - 1, currList + [i], i, result)


########################## Test ###################################
sol = Solution()

########################## combination sum ###################################
print("combination sum test")
print(sol.combinationSum([5, 10, 8, 4, 3, 12, 9], 27))
print("all test are passed!")


########################## combination sum2 ###################################
print("combination sum2 test")
print(sol.combinationSum2([10,1,2,7,6,1,5],8))
print(sol.combinationSum2([1,2,3,4], 6))
print("all test are passed!")

########################## combination sum3 ###################################
print("combination sum3 test")
assert([[1,2,4]] == sol.combinationSum3(7, 3), "wanted: {}\ngot: ".format([[1,2,4]], sol.combinationSum3(7,3)))
assert([[1,2,6], [1,3,5], [2,3,4]] == sol.combinationSum3(9, 3), "wanted: {}\ngot: ".format([[1,2,6], [1,3,5], [2,3,4]], sol.combinationSum3(9,3)))
print("all test are passed!")