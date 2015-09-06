class Solution(object):
    def minCut(self, s):
        """
        minimum way to partition a given string
        : type s: str
        : rtype: int
        """
        pal = self.palindromeGenerate(s)
        pp = [0 for i in range(len(s) + 1)]
        # base case
        pp[len(s) - 1] = 0 # one letter word is already a palindrome
        pp[len(s)] = 0 # no letter word does not need any cut
        # recursive case, not including the base case
        for i in range(len(s) -2, -1, -1):
            if not pal[i][len(s) -1]:
                minimal = float('inf')
                for j in range(i, len(s)):
                    if pal[i][j]:
                        minimal = min(minimal, 1 + pp[j + 1])
                # minimal is the value of the pp[i]
                pp[i] = minimal
        return pp[0]

    def palindromeGenerate(self, s):
        """
        Returns a 2d array of boolean to indicate if s[i:j] is palindrome
        """
        pal = [[False for j in range(len(s))] for i in range(len(s))]
        # base case
        for i in range(len(s)):
            for j in range(i + 1):
                pal[i][j] = True
        # recursive case
        for j in range(len(s)):
            for i in range(j - 1, -1, -1):
                pal[i][j] = s[i] == s[j] and pal[i + 1][j - 1]
        return pal
################################ TEST   #############################
sol = Solution()

############################### is Palindrome test ##########################
print("palindrome test")

arr = sol.palindromeGenerate("s")
arr = sol.palindromeGenerate("bb")
assert(arr[0][1] == True)
arr = sol.palindromeGenerate("aas")
assert(arr[0][1] == True)
assert(arr[1][2] == False)

arr = sol.palindromeGenerate("aaa")
assert(arr[0][2] == True)
assert(arr[1][2] == True)

arr = sol.palindromeGenerate("aabaay")
assert(arr[0][4] == True)

print("all palindrome tests pass!")
############################### is Palindrome test ##########################
print("palindrome partitioning test")
assert(sol.minCut("a") == 0)
assert(sol.minCut("aas") == 1)
assert(sol.minCut("cut") == 2)
assert(sol.minCut("aabaay") == 1)
assert(sol.minCut("bb") == 0)

print("all palindrome minimal partitioning tests pass!")
