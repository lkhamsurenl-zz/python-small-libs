class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        WB = [[""] for i in range(len(s) + 1)] # for all possible ones
        for i in range(len(s) - 1, -1, -1):
            curr = []
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in dict:
                    recList = WB[j]
                    print recList
                    print s[i:j]
                    for string in recList:
                        if not j == len(s):
                            curr.append(s[i:j] + " " + string)
                        else:
                            curr.append(s[i:j])
            WB[i] = curr
        return WB[0]


dict = ["cat", "cats", "and", "sand", "dog"]
s = "catsanddog"
sol = Solution()
print sol.wordBreak(s, dict)
