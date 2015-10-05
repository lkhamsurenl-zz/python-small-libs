class Solution(object):
	def isInterleave(self, s1, s2, s3):
		"""
		check if some formation of s1, s2 interleaving can form s3
		"""
		if len(s1) + len(s2) != len(s3):
			return False
		m = len(s1)
		n = len(s2)
		# II[i][j] is TRUE IFF s1[i:] and s2[j:] can form s3[i+j:] 
		II = [[False for j in range(n + 1)] for i in range(m + 1)]
		# base case
		II[m][n] = True # empty + empty = empty
		for i in range(m -1, -1, -1):
			# does not include s2 at all, and check if s1 == s3
			if s1[i] == s3[n + i]:
				II[i][n] = II[i + 1][n]  
		for j in range(n -1, -1, -1):
			if s2[j] == s3[n + j]:
				II[m][j] = II[m][j + 1]
		# recursive case
		for i in range(m -1, -1, -1):
			for j in range(n -1, -1, -1):
				if s1[i] == s3[i + j]:
					II[i][j] = II[i][j] or II[i + 1][j]
				if s2[j] == s3[i + j]:
					II[i][j] = II[i][j] or II[i][j + 1]
		return II[0][0]

#################				TEST 				#################
print("Testing interleaving")
sol = Solution()
assert(False == sol.isInterleave("s", "a", "a"))
assert(True == sol.isInterleave("a", "a", "aa"))
assert(False == sol.isInterleave("a", "a", "a"))
assert(True == sol.isInterleave("ace", "bdf", "abcdfe"))
