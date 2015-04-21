class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        maxLen = 0 # max length we have seen so far
        leftMatch = -1 # left of current match
        stack = [] # stack to keep track of ( indices
        for j in range(len(s)):
            if s[j] == '(':
                stack.append(j)
            else:
                if len(stack) == 0:
                    leftMatch = j # since there is no matching
                else:
                    stack.pop()
                    if len(stack) == 0:
                        maxLen = max(maxLen, j - leftMatch)
                    else:
                        maxLen = max(maxLen, j - stack[-1])
        return maxLen
sol = Solution()
print sol.longestValidParentheses("(()())()(")
