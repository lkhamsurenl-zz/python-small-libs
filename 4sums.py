import itertools
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num) <= 3:
            return [] # no such possible quadruple
        num.sort() # sort numbers
        val = []
        for lowest in range(len(num) - 3):
            for lower in range(lowest + 1, len(num) - 2):
                low = lower + 1
                high = len(num) - 1
                while low < high:
                    if num[lowest] + num[lower] + num[low] + num[high] == target:
                        val.append([num[lowest] , num[lower] , num[low] , num[high]])
                        low = low + 1
                        high = high - 1
                    elif num[lowest] + num[lower] + num[low] + num[high] < target:
                        low = low + 1
                    else:
                        high = high - 1
        # remove duplicates from the list
        return [i for i, _ in itertools.groupby(val)]

sol = Solution()
print sol.fourSum([1, 0, -1, 0, 2, -2], 0)
