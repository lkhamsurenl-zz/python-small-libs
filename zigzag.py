class Solution:
    # @return a string
    def convert(self, s, nRows):
        lst = [[] for i in range(nRows)]
        listInd = 0
        i = 0
        while i < len(s):
            if listInd % 2 == 0 and len(lst[listInd]) % 2 != 0:
                lst[listInd].append(".")
            else:
                lst[listInd].append(s[i])
                i = i + 1
            listInd = (listInd + 1) % nRows
        # replace . with ""
        for i in range(len(lst)):
            lst[i] = [x for x in lst[i] if x != "."]
        s = ""
        for str in lst:
            s = s + "".join(str)
        return s

sol = Solution()
print sol.convert("" , 7)
