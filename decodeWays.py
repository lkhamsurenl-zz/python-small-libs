class Solution(object):
	def numDecodings(self, s):
		"""
		Count number of ways to decode the given number string
		A -> 1
		B -> 2
		...
		Z -> 26
		"""
		if len(s) == 0 or (len(s) == 1 and s == "0"):
			return 0
		n = len(s)
		# base
		prev2 = 1
		prev1 = 1 if s[n - 1] != "0" else 0 # 1 only if not 0
		# recursive case
		for i in range(n - 2, -1, -1):
			temp = 0 
			if s[i] != 0:
				temp += prev1
				if 1 <= int(s[i:i + 2]) <= 26:
					temp += prev2
			prev2 = prev1 
			prev1 = temp
		return prev1


###################################### TEST ###################################
sol = Solution()
print("Testing num of ways to decodings")
print(sol.numDecodings("0"))
assert(0 == sol.numDecodings("0"))

print(sol.numDecodings("12"))
assert(2 == sol.numDecodings("12"))

print(sol.numDecodings("12"))
assert(2 == sol.numDecodings("12"))

print(sol.numDecodings("123"))
assert(3 == sol.numDecodings("123"))