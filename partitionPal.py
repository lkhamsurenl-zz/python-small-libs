import copy, itertools
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s) == 0:
            return []
        return self.recPartPal(s, 0, len(s) - 1)

    def recPartPal(self, s, low, high):
        if low > high:
            return [[]]
        if low == high:
            return [[s[low]]]
        currList = []
        for i in range(low, high + 1):
            recList = self.recPartPal(s, i +1, high)
            if recList is not None and self.isPal(s, low, i):
                for lst in recList:
                    newList = copy.deepcopy(lst)
                    newList.insert(0, s[low:i + 1])
                    currList.append(newList)
        return [i for i, _ in itertools.groupby(currList)]

    def isPal(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low = low + 1
            high = high - 1
        return True

sol = Solution()
print sol.partition("amanaplanacanalpanama")
