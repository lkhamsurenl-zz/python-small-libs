class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):

    def recIsMatch(self, s, p, i):
        if i >= len(s):
            return True
        if s[i + 1] == '*' or p[i + 1] == '*':
