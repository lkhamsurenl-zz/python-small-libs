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

    def palindromePartition(self, s):
        """
        Given a string, return all possible ways to partition to palindromes
        """
        output = []
        self.__recPartitionPalindrome__(s, 0, [], output)
        return output

    def __recPartitionPalindrome__(self, s, i, curr, output):
        if i == len(s):
            output.append(curr)
            return
        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):
                lst = [num for num in curr]
                lst.append(s[i:j+1])
                self.__recPartitionPalindrome__(s, j + 1, lst, output)

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
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

############################### is Palindrome test ##########################
for (s, want) in [ ("a", [["a"]]), ("aab", [["a", "a", "b"], ["aa", "b"]]),\
                ("", [[]]), ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]) ]:
    got = sol.palindromePartition(s)
    assert got == want, \
        "palindromePartition({}) = {}; want: {}".format(s, got, want)

print("all palindrome partitioning tests pass!")
