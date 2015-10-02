import copy
import itertools
class Solution(object):
	out = []
	def combinationSum(self, candidates, target):
		self.recCom(candidates, 0, target, [0 for i in range(len(candidates))])
		return self.out

	def recCom(self, candidates, index, target, currList):
		if target < 0 or index < len(candidates):
			return
		if target == 0:
			lst = []
			for i in range(len(currList)):
				time = currList[i] # candidates[i] should appear time in list
				lst = lst + [candidates[i] for j in range(time)]
			self.out.append(lst)
			return
		times = 0
		while times * candidates[index] <= target:
			newList = copy.deepcopy(currList)
			newList[index] = times
			self.recCom(candidates, index + 1, target - times * candidates[index], newList)
			times += 1

########################## Test ###################################
sol = Solution()

########################## combination sum ###################################
print("combination sum test")
print(sol.combinationSum([5, 10, 8, 4, 3, 12, 9], 27))
print("all test are passed!")
