class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        length = self.findCommonMinLength(strs)
        pre = ""
        for ind in range(length):
            common = strs[0][ind]
            for s in strs:
                if s[ind] != common:
                    return pre
            # all common
            pre = pre + common
        return pre
    # find length of the shortest string in list
    def findCommonMinLength(self, strs):
        minimal = len(strs[0])
        for s in strs:
            if len(s) < minimal:
                minimal = len(s)
        return minimal

sol = Solution()
# no strs
print("no string in the length: {} for {}".format(sol.longestCommonPrefix([]), []))
# little common
print("no string in the length: {} for {}".format(sol.longestCommonPrefix(["a", "ab"]), ["a", "ab"]))
