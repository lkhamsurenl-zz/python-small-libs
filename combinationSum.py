import copy
class Solution(object):
	sol = []
	def combinationSum3(self, k, n):
		self.recCom(0, k, n, [])
		return self.sol

	def recCom(self, i, k, n, currList):
		if i > 9: 
			if k != 0 or n != 0:
				return
			else:
				self.sol.append(currList)
				return 
		else:
			# current index is included
			newList = copy.deepcopy(currList)
			newList.append(i)
			self.recCom(i + 1, k - 1, n - i, newList)
			# not included
			self.recCom(i + 1, k, n, currList)

########################## Test ###################################
sol = Solution()

########################## combination sum ###################################
print("combination sum test")
assert([[1,2,4]] == sol.combinationSum3(3,7))
assert([[1,2,6], [1,3,5], [2,3,4]] == sol.combinationSum3(3,9))
print("all test are passed!")
