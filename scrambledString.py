class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        n = len(s1)
        S = [[[False for l in range(n + 1)] for j in range(n)] for i in range(n)]
        # S[i][j][l] = True if s1[i:i+l] scramble of s2[j:j+l]
        # base case
        for i in range(n):
            for j in range(n):
                S[i][j][1] = s1[i] == s2[j]
        # recursive
        for l in range(1, n + 1):
            for i in range(0, n - l + 1):
                for j in range(0, n - l + 1):
                    for k in range(1, l):
                        if S[i][j][k] and S[i + k][j + k][l - k]:
                            S[i][j][l] = True # no scrambling at the length k
                        if S[i][j + l - k][k] and S[i + k][j][l - k]:
                            S[i][j][l] = True # scrambled at the length k
        return S[0][0][n]

sol = Solution()
for (s1, s2, want) in [ ("a", "a", True), ("abc", "cba", True), ("abcd", "bdac", False) ]:
    got = sol.isScramble(s1, s2)
    assert got == want, \
        "isScramble({}, {}) = {}; want {}".format(s1, s2, got, want)
