# find the length of the longest pal substring in a given string
# IDEA: when add one character to an string, we can increase the man length of pal substring by at most 2. So we can traverse and check if the latter addition forms pal
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        maxLen = 0 # max length of pal substring
        palString = ""
        for i in xrange(len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1: i + 1][::-1]:
                palString = s[i - maxLen - 1: i +1]
                maxLen = maxLen + 2
                continue
            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen: i + 1][::-1]:
                palString = s[i - maxLen: i +1]
                maxLen = maxLen + 1
        return palString

sol = Solution()
for s in ["a", "aba", "aac", "weed", "aaaaaaaaab", "aaaaabaaa"]:
    print("longest in {} is : {}".format(s, sol.longestPalindrome(s)))
