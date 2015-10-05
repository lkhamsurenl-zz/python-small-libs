class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) == 0 or len(t) == 0:
        	return 0
        m = len(s) # s is the smaller one
        n = len(t) # contains s
        IN = [[0 for j in range(n + 1)] for i in range(m + 1)]
        # base case
        for i in range(m + 1):
        	IN[i][n] = 0 
        for j in range(n + 1):
        	IN[m][j] = 1
        # recursive 
        for j in range(n - 1, -1, -1):
        	for i in range(m - 1, -1, - 1):
        		if s[i] == t[j]:
        			# two ways to go, either comsume current place
        			# or take the next rec

        			IN[i][j] += IN[i + 1][j + 1]
        		# no match for t[i] in s[j], so move on 
        		IN[i][j] += IN[i][j + 1]
        		print("i: {}, j: {}, and value: {}".format(i, j, IN[i][j]))
        return IN[0][0]


#####################          	TEST 				$#####################
sol = Solution()
print("Testing number of distinct subsequences")
print("s: {}, t: {}, and: {}".format("ab", "ab", sol.numDistinct("ab", "ab")))
print("s: {}, t: {}, and: {}".format("ab", "abb", sol.numDistinct("ab", "abb")))
print("s: {}, t: {}, and: {}".format("rabbit", "rabbbit", sol.numDistinct("rabbit", "rabbbit")))
print("Passed the test")