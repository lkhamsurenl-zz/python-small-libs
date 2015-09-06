class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        # Keep track of the (low, high) of longest substring up until now
        mapping = {}
        low = 0
        length = 0
        for i in range(len(s)):
            if s[i] in mapping and mapping[s[i]] >= low:
                low = mapping[s[i]] + 1
            mapping[s[i]] = i
            length = max(length, i - low + 1)
        return length

sol = Solution()
print("longest of {} is {}".format("abc", sol.lengthOfLongestSubstring("abc")))
print("longest of {} is {}".format("abcabc", sol.lengthOfLongestSubstring("abcabc")))
print("longest of {} is {}".format("aab", sol.lengthOfLongestSubstring("aab")))
print("longest of {} is {}".format("cdd", sol.lengthOfLongestSubstring("cdd")))
