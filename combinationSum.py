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