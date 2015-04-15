class Solution:
    # @return an integer
    def romanToInt(self, s):
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        lst = []
        for char in s:
            lst.append(dic[char]) # get list of numbers
        # NOTE: If there is an descending then it's special number like 4, 9, 90, 89
        i = 0
        ans = 0
        while i < len(s) - 1:
            if lst[i] >= lst[i + 1]:
                ans = ans + lst[i]
                i  = i + 1
            else:
                ans = ans + (lst[i + 1] - lst[i])
                i = i + 2
        # check for the last number
        if i < len(s):
            ans = ans + lst[i]
        return ans

sol = Solution()
for s in ["I", "X", "IV", "VIII", "CL", "XC" , "MDCCC"]:
    print sol.romanToInt(s)
