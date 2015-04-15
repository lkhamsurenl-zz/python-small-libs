class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        n = len(s1)
        scramble = [False for i in range(n + 1)]
        # base
        scramble[n] = True
        # non-base
        for i in range(n -1, -1 , -1):
            isScramble = False
            for j in range(i + 1, n + 1):
                isScramble = isScramble or (self.isRotation(s1, s2, i, j) and scramble[j])
            scramble[i] = isScramble
        return scramble[0]

    # checks if s2[i:j] rotation of s1[i:j]
    def isRotation(self, s1, s2, i , j):
        print("({}, {})".format(s1[i:j] , s2[i:j]))
        # rotation if s2[i:j] if s2s2 has s1 as a substring
        return s1[i:j] in (s2[i:j] + s2[i:j])

sol = Solution()
print sol.isScramble("abc", "cba")
