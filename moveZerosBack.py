class Solution:
	def moveZeros(self, nums):
		"""
		move all zeros to the back
		"""
		i = 0
		j = 0
		while j < len(nums):
			if nums[j] != 0:
				nums[i] = nums[j]
				i += 1
			j += 1
		# put all 0 after the until i hit the end
		while i < len(nums):
			nums[i] = 0
			i += 1
sol = Solution()
######################## TEST ############################
print("Testing moveZeros")
arr = [0, 1, 2, 3, 0]
sol.moveZeros(arr)
assert([1,2,3, 0,0] == arr)

arr = [0]
sol.moveZeros(arr)
assert([0] == arr)

arr  = [1,2,3]
sol.moveZeros(arr)
assert([1,2,3] == arr)